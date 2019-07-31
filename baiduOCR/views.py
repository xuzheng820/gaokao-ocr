from django.http import HttpResponse
from django.shortcuts import render
from baiduOCR.forms import FileUploadForm
from aip import AipOcr
import json

def upload_file(request):
    """
    文件接收 view
    :param request: 请求
    :return:
    """
    if request.method == 'POST':
        my_form = FileUploadForm(request.POST, request.FILES)
        if my_form.is_valid():
            f = my_form.cleaned_data['my_file']
            ret = handle_uploaded_file(f)
        return HttpResponse(ret)
    else:
        my_form = FileUploadForm()
    return render(request, 'upload.html', {'form': my_form})


def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return baidu_ocr_api(f)

def baidu_ocr_api(f):
    APP_ID = '16825035'
    API_KEY = 'YqAPEsqSTGHZ77X1doStnOhP'
    SECRET_KEY = 'Lc2k3GahVxe4UM79Hbkcs0CoNZKBfQSh'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


    image = get_file_content(f.name)
    reply = client.handwriting(image)
    ret = ""
    for item in reply['words_result']:
        ret += item['words'] + '<br>'
    return ret


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

