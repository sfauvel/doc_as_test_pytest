import os
import sys
import glob
import json
import shutil
import json

class DocGenerator():
    OUTPUT_FOLDER = "docs"

    def __init__(self, request, description):
        self.buffer=""
        self.testname = request.node.name
        self.description = description
        if (not description):
            self.description = self.testname

    def doc_file_name(self):
        return self.testname[len("test_"):] + ".adoc"

    def doc_file_path(self):
        return DocGenerator.OUTPUT_FOLDER + "/" + self.doc_file_name()

    def finish(self):        
        with open(self.doc_file_path(), "w") as f:
            f.write(self.doc_content())
       
    def title(self):
        name = self.testname[len("test_"):]
        name = name.replace("_", " ")
        name = name[0].upper() + name[1:]
        return name

    def doc_content(self):
        title = "= " + self.title() +"\n\n"
        description = self.description.strip() +"\n\n" if self.description != None else ""
        content = self.buffer +"\n\n"

        return  title + description + content
 
    def write(self, text):
        self.buffer = self.buffer + text


class FullDocGenerator():
    OUTPUT_FOLDER = "docs"
    
    def __init__(self, file_name):
        self.file_name = file_name
        self.test_files = []
     
    def doc_file_name(self):
        return self.file_name

    def doc_file_path(self):
        return DocGenerator.OUTPUT_FOLDER + "/" + self.doc_file_name()

    def finish(self):        
        with open(self.doc_file_path(), "w") as f:
            f.write(self.doc_content())
    
    def title(self):       
        return "Full doc"

    def content(self):
        return '\n'.join("include::{}[leveloffset=+1]".format(file) for file in self.test_files)

    def doc_content(self):
        title = "= " + self.title() +"\n\n"
        content = self.content() +"\n\n"

        return  title + content
 
    def register(self, file_name):
        self.test_files.append(file_name)