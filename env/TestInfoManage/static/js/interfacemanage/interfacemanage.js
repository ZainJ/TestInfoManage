/**
 * Created by Administrator on 2018/8/17.
 */
(function(){
    $(a.interfacelist).click(function(){
        $.get('/interfacelist/',function(data,status){
            data=data;
            status=status;
        })
    })
});