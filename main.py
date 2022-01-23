brackets = {
    '(': ')',
    '[': ']',
    '{': '}'
}

balanced = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
unbalanced = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]

class Stack(list):

    def isEmpty(self):
        return len(self) == 0

    def push(self, _item):
        self.append(_item)

    def pop(self):
        if not self.isEmpty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item

    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)


def check(my_stack):
    stack = Stack()
    for i in my_stack:
        if i in brackets:
            stack.push(i)
        elif i == brackets.get(stack.peek()):
                stack.pop()
            else:
                return "False"
        return stack.isEmpty()
 
if __name__ == '__main__':
    for seq in balanced + unbalanced:
        print(f'{seq:<30}{check(seq)}')
