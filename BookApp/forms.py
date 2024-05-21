from django import forms


class RegisterForm(forms.Form):
    '''
    验证用户注册数据
    '''
    username = forms.CharField(min_length= 3, max_length= 15,
                               error_messages= {
                                   'min_length': '用户名长度不足',
                                   'max_length': '用户名长度过长',
                                   'required': '用户名不允许为空',
                               })
    password = forms.CharField(min_length= 6, max_length= 15,
                               error_messages= {
                                   'min_length': '密码长度不足',
                                   'max_length': '密码长度过长',
                                   'required': '密码不允许为空',
                               })
    resetpw = forms.CharField(min_length= 6, max_length= 15,
                               error_messages= {
                                   'min_length': '密码长度不足',
                                   'max_length': '密码长度过长',
                                   'required': '密码不允许为空',
                               })
    email = forms.EmailField(error_messages= {'invalid': '邮箱格式不正确',
                                              'required': '邮箱不允许为空',})


    def clean(self):
        pwd1 = self.cleaned_data.get('password')
        pwd2 = self.cleaned_data.get('resetpw')
        if pwd1 != pwd2:
            self.add_error('resetpw', '两次密码输入不一致')
        return self.cleaned_data


class LoginForm(forms.Form):
    '''
    验证用户登录数据
    '''


    username = forms.CharField(min_length= 3, max_length= 15,
                               error_messages= {
                                   'min_length': '用户名长度不足',
                                   'max_length': '用户名长度过长',
                                   'required': '用户名不允许为空',
                               })
    password = forms.CharField(min_length= 6, max_length= 15,
                               error_messages= {
                                   'min_length': '密码长度不足',
                                   'max_length': '密码长度过长',
                                   'required': '密码不允许为空',
                               })