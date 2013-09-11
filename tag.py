
'''
    See reference: http://www.javascriptkit.com/domref/elementproperties.shtml
'''

class Tag(object):

    def __init__(self, tagname):
        self.tagname = tagname

    def __call__(self, *inner, **kwargs):
        return Element(self.tagname, inner, **kwargs)

class EmptyTag(Tag):

    def __call__(self, *inner, **kwargs):
        return EmptyElement(self.tagname, **kwargs)


class Element(object):

    def __init__(self, tagname, inner, **kwargs):
        self.tagname = tagname
        self.inner = inner
        if 'class_' in kwargs:
            kwargs['class'] = kwargs.pop('class_')
        self.args = kwargs

    def __unicode__(self):
        inner = u'\n'.join(unicode(i) for i in self.inner)
        return u'<{} '.format(self.tagname) \
             + u' '.join(key + u'="' + self.args[key] + u'"' for key in self.args) \
             + u'>\n{}\n</{}>'.format(inner, self.tagname)

    def __str__(self):
        return self.__unicode__()

    def __iter__(self):
        'Hack to be returned to CherryPy with no prior conversion'
        class TagIterator(object):

            def __init__(self, parent):
                self.stop = False
                self.parent = parent

            def next(self):
                if self.stop:
                    raise StopIteration
                else:
                    self.stop = True
                    return unicode(self.parent)

        return TagIterator(self)

class EmptyElement(Element):

    def __init__(self, tagname, **kwargs):
        self.tagname = tagname
        if 'class_' in kwargs:
            kwargs['class'] = kwargs.pop('class_')
        self.args = kwargs

    def __unicode__(self):
        return u'<{} '.format(self.tagname) + u' '.join(key + u'="' + self.args[key] + u'"' for key in self.args) + u' />'

