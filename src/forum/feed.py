﻿#!/usr/bin/env python
#encoding:utf-8
#-------------------------------------------------------------------------------
# Name:        Syndication feed class for subsribtion
# Purpose:
#
# Author:      Mike
#
# Created:     29/01/2009
# Copyright:   (c) CNPROG.COM 2009
# Licence:     GPL V2
#-------------------------------------------------------------------------------
from django.contrib.syndication.feeds import Feed
from models import Question
from django.template.defaultfilters import slugify
from settings import MY_URL


class RssLastestQuestionsFeed(Feed):
    title = u"Mendix Forum"
    link = MY_URL
    description = u"The place where modelers and developers meet to discuss, ask and answer Mendix related questions and topics."
    #ttl = 10
    #copyright = u'Copyright(c)2009.CNPROG.COM'
    copyright = u'Copyright(c)2009.MENDIX.COM'

    def item_link(self, item):
        return "%s/questions/%s/%s/" % (self.link, item.id, slugify(item.title))

    def item_author_name(self, item):
        return item.author.real_name

    def item_author_link(self, item):
        return '/users/%s/%s' % (item.author.id, item.author.real_name)

    def item_pubdate(self, item):
        return item.added_at

    def items(self, item):
        return Question.objects.filter(deleted=False).order_by('-added_at')[:30]


def main():
    pass

if __name__ == '__main__':
    main()
