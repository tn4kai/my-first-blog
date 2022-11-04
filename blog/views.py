from django.shortcuts import render
from django.utils import timezone
# models.pyのモデルをインクルード
# .はカレントディレクトリ(拡張子は不要)
from .models import Post

# Create your views here.

# 投稿の一覧を表示
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # {} の中に引数を記述する時は、名前と値をセット('posts'が名前で、後ろの方の posts は値、クエリセット)
    return render(request, 'blog/post_list.html', {'posts': posts})