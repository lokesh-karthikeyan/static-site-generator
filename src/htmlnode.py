class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props:
            return ' ' + ' '.join(f'{key}="{value}"' for key, value in self.props.items())

        return ''

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, children=[], props = props)

        if value is None:
            raise ValueError("All leaf nodes must have a value")

    def to_html(self):
        if not self.tag:
            return self.value

        attrs = self.props_to_html()

        return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag, value = None, children = children, props = {})

        if not tag:
            raise ValueError("All parent nodes must have a tag")
        if not children:
            raise ValueError("A parent node must have at least one child node")

    def to_html(self):
        attrs = self.props_to_html()
        opening_tag = f'<{self.tag}{attrs}>'

        children_html = ''.join([child.to_html() for child in self.children])

        return f'{opening_tag}{children_html}</{self.tag}>'
