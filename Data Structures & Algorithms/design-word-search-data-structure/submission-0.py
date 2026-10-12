class Tree:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = Tree()

    def addWord(self, word: str) -> None:
        node = self.root

        for w in word:
            if w not in node.children:
                node.children[w] = Tree()
            node = node.children[w]
        
        node.is_end = True
        
        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.is_end

            w = word[i]

            if w == ".":
                for child in node.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

            if w not in node.children:
                return False

            return dfs(i + 1, node.children[w])
        return dfs(0, self.root)
        
