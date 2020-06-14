from typing import List


class Node:
    def __init__(self, name: str):
        self.name = name


class FolderNode(Node):
    def __init__(self, name: str):
        super().__init__(name)
        self.children = []


class FileNode(Node):
    def __init__(self, name: str, content: str = ""):
        super().__init__(name)
        self.content = content


class FileSystem:

    def __init__(self):
        self.head = FolderNode("")
        self.paths = {"/": self.head, "": self.head}

    def ls(self, path: str) -> List[str]:
        node = self.paths[path]
        if isinstance(node, FileNode):
            return [node.name]
        return sorted(self.paths[path].children)

    def mkdir(self, path: str) -> None:
        curr = ""
        prev = self.head
        for folder_name in path.split("/")[1:]:
            curr += "/" + folder_name
            if curr not in self.paths:
                self.paths[curr] = FolderNode(folder_name)
                prev.children.append(self.paths[curr].name)
            prev = self.paths[curr]

    def addContentToFile(self, file_path: str, content: str) -> None:
        if file_path in self.paths:
            file = self.paths[file_path]
            file.content += content
        else:
            folder_path, filename = file_path.rsplit('/', 1)
            self.paths[file_path] = FileNode(filename, content)
            folder = self.paths[folder_path]
            folder.children.append(filename)

    def readContentFromFile(self, file_path: str) -> str:
        return self.paths[file_path].content

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)