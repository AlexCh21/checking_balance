open_list = ["[","{","("]
close_list = ["]","}",")"]

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
    stack = []
    for i in my_stack:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "False"
    if len(stack) == 0: 
        return "True"
 
if __name__ == '__main__':
    for seq in balanced + unbalanced:
        print(f'{seq:<30}{check(seq)}')