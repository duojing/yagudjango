from django.shortcuts import render, get_object_or_404, redirect
from yagudjango.models import Gujang, Block, Seat, Comment
from django.views.generic import DetailView
from yagudjango.forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def gujang_list(request):
    name_select = request.GET.get('name_select', '')
    name_set = Gujang.objects.all()

    if name_select :
        name_set = name_set.filter(name__icontains=name_select)
    return render(request, 'yagudjango/gujang_list.html',{
        'name_select' : name_select,
        'name_set' : name_set,
        })

def gujang_detail(request, id):
    gujang = Gujang.objects.get(id=id)
    return render(request, 'yagudjango/gujang_detail.html',{
        'gujang': gujang,
    })

def index(request):
    block_list = Block.objects.all()
    return render(request, 'yagudjango/block_list.html',{
        'block_list':block_list,
    })

block_detail = DetailView.as_view(model=Block)

@login_required
def comment_new(request, post_pk):
    post = get_object_or_404(Block, pk=post_pk)

    if request.method =='POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            if request.is_ajax():
                return render(request, 'yagudjango/_comment.html',{
                    'comment':comment,
                })
            messages.success(request, '새 댓글을 저장했습니다.')
            return redirect(comment.post)
    else:
        form = CommentForm()
    return render(request, 'yagudjango/comment_form.html',{
        'form':form,
    })

@login_required
def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.user != request.user:
        messages.warning(request, '댓글 작성자만 수정할 수 있습니다.')
        return redirect(comment.post)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save()
            messages.success(request, '기존 댓글을 수정했습니다.')
            return redirect(comment.post)

    else:
        form = CommentForm(instance=comment)
    return render(request, 'yagudjango/comment_form.html',{
        'form':form,
    })

@login_required
def comment_delete(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.user != request.user:
        messages.warning(request, '댓글 작성자만 삭제할 수 있습니다.')
        return redirect(comment.post)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, '댓글을 삭제했습니다.')
        return redirect(comment.post)
    return render(request, 'yagudjango/comment_confirm_delete.html',{
        'comment':comment,
    })

def main(request):
    return render(request, 'yagudjango/yagudjango_main.html')

