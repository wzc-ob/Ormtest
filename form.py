from django import forms
from django.core import validators
from Test.models import Score, Student
from django.http import HttpResponse

class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=3, label='标题', min_length=2, error_messages={"min_length": '标题字符段不符合要求！'})
    content = forms.CharField(widget=forms.Textarea, label='内容')
    email = forms.EmailField(label='邮箱')
    reply = forms.BooleanField(required=False, label='回复')
    telephone = forms.CharField(max_length=11,validators=[validators.RegexValidator('[1][3,4,5,7,8][0-9]\\d{8}',message='请输入正确格式的手机号码！')])
    pwd1 = forms.CharField(max_length=12)
    pwd2 = forms.CharField(max_length=12)
    # 验证数据库中该手机好是否被注册过了
    # def clean_telephone(self):
        # telephone = self.cleaned_data.get('telephone')
        # exists = Student.objects.filter(telphone= telephone).exists()
        # print(exists)
        # if  exists :
        #     raise forms.ValidationError('手机号码已经存在')

        # return telephone
    # 多个字段验证比如判断密码是否相等
    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError('两次输入的密码不相同')
class Myform(forms.ModelForm):
    class Meta:
        model  =  Student
        fields = ['name','gender','telphone','file']
        error_messages = {
            'name ':{'max_length ':'最多不能超过十个字符'},
            'telphone':{'required':'必须输入telphone'}
        }
