/**
 * Created by Administrator on 2018/8/22.
 */

function openmodal(){
        layui.use('layer',function(){
           var layer=layui.layer;
            layer.open({
                type:1,
                title:"添加项目",
                area:['800px','600px'],
                shadeClose:false,
                content: $('#projectform')
            })
        });
}
function refresh(){
                    location.reload(true);
                }
$(function() {
    //添加项目
    $('#submit').click(function (event) {
        event.preventDefault();
        var project = $("input[name=project]");
        var creater = $('input[name=creater]');
        var projectdescription = $('textarea[name=projectdescription]');

        var projectV = project.val();
        var createrV = creater.val();
        var projectdescriptionV = projectdescription.val();
        zlajax.post({
            "url": '/project/',
            'data': {
                'project': projectV,
                'creater': createrV,
                'projectdescription': projectdescriptionV
            },
            'success': function (data) {
                if (data['code'] == '200') {
                    $('#message').html(data['message']);
                    setTimeout('refresh()', 2000);
                } else if (data['code'] == '403') {
                    $('#message').html(data['message']);
                }
            },
            'fail': function (error) {
                xtalert.alertNetworkError();
            }
        })
    });

});

function searchproject(){
    var projectname=$("input[name=projectname]");
    var projrctmanager=$("input[name=projrctmanager]");
    var  projectnamev=projectname.val();
    var projrctmanagerv=projrctmanager.val();
    $("tbody").empty();
    zlajax.post()

}

