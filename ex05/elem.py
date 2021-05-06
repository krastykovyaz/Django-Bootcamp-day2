class Text(str):

    def __str__(self):
        exchange = super().__str__().replace('>', '&gt;').replace('<', '&lt;')
        if exchange == '"':
            exchange = exchange.replace('"', '&quot;')
        return exchange.replace('\n', '\n<br />\n')


class Elem:

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        if not isinstance(content, (Text, Elem)):
            if type(content) != list and type(content) != None.__class__:
                raise self.ValidationError()
        self.content = [content] if not type(content) == list else content
        self.attr = attr
        self.type = tag_type
        self.space = 0
        self.tag = tag

    class ValidationError(Exception):
        def __init__(self):
            Exception.__init__(self, "Error")

    def __str__(self):
        html = self.create_content()
        if_content = "\n%s</%s>" % ("  " * self.space, self.tag) if self.create_content()\
            else "</%s>" % self.tag
        if self.type == 'double':
            return "<%s%s>%s%s" % (self.tag, self.create_attr(), html, if_content)
        else:
            return "<%s%s/>%s" % (self.tag, self.create_attr(), html)

    def create_attr(self):
        attr_html = ''
        for k, v in self.attr.items():
            attr_html += ''' %s=\"%s\"''' % (k, str(v))
        return attr_html

    def create_content(self):
        content_html = ''
        for item in self.content:
            if isinstance(item, Elem):
                self.set_space(item)
            if item:
                content_html += "\n  %s%s" % ("  " * self.space, str(item))
        return content_html

    def set_space(self, elem):
        if isinstance(elem, Elem):
            elem.space += 1
        if isinstance(elem.content[0], Elem):
            elem.set_space(elem.content[0])

    def add_content(self, content):
        if isinstance(content, (Elem, Text)):
            self.content.append(content)
        else:
            raise self.ValidationError()
