from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm


def post_comment(request, post_pk):
    # 获取评论文章，因为后面需要把评论和被评论的文章关联起来
    # get_object_or_404 快捷表示存在或者返回404
    post = get_object_or_404(Post, pk=post_pk)

    # post 处理表单数据
    if request.method == 'POST':
        # 构建CommentForm 实例，创造Django 表单
        form = CommentForm(request.POST)

        # 调用设定的 is_valid() 方法自动检查数据是否符合格式要求
        if form.is_valid():
            comment = form.save(commit=False)

            comment.post = post

            comment.save()

            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list,
            }
            return render(request, 'blog/detail.html', context=context)

    return redirect(post)