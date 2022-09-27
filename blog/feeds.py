from django.urls import reverse_lazy
from django.contrib.syndication.views import Feed
from .models import Post


class PostFeed(Feed):
    title = 'PythonTuts+'
    description = 'PythonTuts+, articles about python'
    link = reverse_lazy('blog:post_list')

    def items(self):
        return Post.published.all()

    def item_title(self, item):
        return item.title

    def item_desscription(self, item):
        return item.body

    def item_pubdate(self, item):
        return item.publish
