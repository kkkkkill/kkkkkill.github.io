let vm = new Vue({

    //通过html的选择器进行绑定
    el: '#zc',

    //修改vue的模板语法
    delimiters: ['[[',']]'],

    data: {
        username:'',
        password:'',
        resetpw:'',
        image_code_url:'',

        error_name:false,
        error_password:false,
        error_resetpw:false,

        error_nmae_message:'',
        error_password_message:'',
        error_resetpw_message:'',
    },

    //这个方法在html执行的时候会被调用
    mounted(){
        this.image_code()
    },

    //定义事件方法
    methods: {
        //生成图片验证码
        image_code(){
            this.image_code_url = '/image/?'+ new Date().getTime()
        },
        //校验用户名数据
        check_name(){
            //定义用户名的规则范围
            let re =/^[A-Za-z0-9_]{3,15}$/
            //判断用户名是否满足定义的规则
            if(re.test(this.username)){
                //用户名合法
                this.error_name = false;
            }else {
                //用户名不合法
                this.error_name = true;
                this.error_nmae_message = '用户名不合法'
            }
            //判断用户名是否重复
            //前提保证用户名是合法
            if (this.error_name == false){
                //发送ajax请求
                axios.get(
                    '/count/'+this.username+'/',
                    {responseType:'json'}
                )
                    .then(response =>{
                        //获取后端传递过来的数据
                        if (response.data.count > 0){
                            //用户名存在
                            this.error_name = true;
                            this.error_nmae_message = '用户名已存在'
                        }else {
                            this.error_name = false;
                        }
                    })
                    .catch(error =>{
                        console.log(error.response)
                    })
            }
        },
        //校验密码
        check_password(){
            let re =/^[A-Za-z0-9_]{6,15}$/
            if(re.test(this.password)){
                //密码合法
                this.error_password = false;
            }else {
                //密码不合法
                this.error_password = true;
                this.error_password_message = '密码不合法'
            }
        },
        //校验两次密码是否一致
        check_resetpw(){
            if (this.password == this.resetpw){
                this.error_resetpw = false;
            }else {
                this.error_resetpw = true;
                this.error_resetpw_message = '两次密码不一致'
            }
        },

        //表单是否允许提交的操作
        on_submit(){
            //调用所有的方法
            this.check_name()
            this.check_password()
            this.check_resetpw()
            //判断error对应的值是否为true， 如果其中有一个为true则不允许提交
            if(this.error_name == true|| this.error_password == true || this.error_resetpw == true){
                //禁止表单提交的方法
                window.event.returnValue = false;
            }

        }
    }
})