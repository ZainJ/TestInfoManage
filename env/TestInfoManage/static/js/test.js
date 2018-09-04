/**
 * Created by Administrator on 2018/8/27.
 */
//装变量的容器,可以使用多个分页器哦!
var dataObj = {
    page_enterprise : 1,
    page_order : 1,
    page_log: 1,
    page_log_info: 1,
    limit_enterprise: 10,
    limit_order: 10,
    limit_log:   10,
    limit_log_info: 10
}
//可以多个分页在同一个页面中,只要给其不同的id容器即可

function GetEnterprise(page){
    //初始化的时候直接为1,GetEnterprise(1)(之后数据变更,影响数据结构如:减少或者更改状态等直接直接调取GetEnterprise(dataObj.page_enterprise):刷新当前页数据)
    if (token == null || token == "") {
        return;
    }
    var status =  $("#SelectEnterpriseStatus").val();
    var enterpriseName = $("#txtEnterpriseName").val();
    GetSaleData("get",  "Sale/GetSaleEnterprise",{
        status: status,
        enterpriseName: enterpriseName,
        saleUserID: enterpriseSaleUserID,
        pageIndex: page,
        pageSize: dataObj.limit_enterprise   //可以选择每页显示的数据条数,这个所以就是动态的了
    },function (d) {
        if (d.status == -1) {
            artDialog.alert("系统提示：" + d.message);
            return;
        }
        var total = d.data.total;
        if (d.data.info.length == 0) {
            $("#tbodyEnterprise").html("");
            return;
        }
        $("#tbodyEnterprise").html("");
        var html = "";
        for (i = 0; i < d.data.info.length; i++) {
            var enterprise = d.data.info[i];
            html += '<tr>';
            html += '<td>' + ResetNull(enterprise.EnterpriseName) + '</td>';
            html += '<td>' + ResetNull(enterprise.AdminUserName) + '</td>';
            html += '<td>' + ResetNull(enterprise.ContactsMoblie) + '</td>';
            html += '<td '
            if (enterprise.SaleUserID !=null)
            html += ' onclick="EnterpriseQueryBySale(\'' + enterprise.SaleUserID + '\')" ';
            html += ' class="t_form_ssxs">' + ResetNull(enterprise.SaleUserName) + '</td>';
            html += '<td>' + ResetNull(enterprise.SaleMoblie) + '</td>';
            html += '<td>' + ResetNull(enterprise.CreatedByUserName);
            if (enterprise.IsYuanGong != '') html += '<span style="color:red;">(' + enterprise.IsYuanGong + ')</span>'
            html += '</td>';
            html += '<td>' + enterprise.CreatedDateTime + '</td>';
            html += '<td>' + enterprise.EnterpriseStatusName + '</td>';
            html += '<td>';
            html += '<button type="button" class="btn btn-default btn-sm" onclick="EnterpriseView(\'' + enterprise.EnterpriseID + '\')">';
            html += '<span class="fa fa-eye"></span> 查看';
            html += '</button>';
            html += '<button type="button" class="btn btn-default btn-sm" onclick="EnterpriseSet(\'' + enterprise.EnterpriseID + '\')">';
            html += '<span class="fa fa-eye"></span> 管理';
            html += '</button>';
            html += '<button type="button" class="btn btn-default btn-sm" onclick="OrderList(\'' + enterprise.EnterpriseName + '\')">';
            html += '<span class="fa fa-eye"></span> 订单';
            html += '</button>';
            html += '<button type="button" class="btn btn-default btn-sm"  onclick="SetSale(\'' + enterprise.EnterpriseID + '\',1)">';
            html += '<span class="fa fa-exchange"></span> 分配销售';
            html += '</button>';
            html += '<button type="button" class="btn btn-default btn-sm" onclick="EnterpriseDel(\'' + enterprise.EnterpriseID + '\',\'' + enterprise.EnterpriseName + '\')">';
            html += '<span class="fa fa-eye"></span> 删除';
            html += '</button>';
            html += '</td>';
            html += '</tr>';
        }
        $("#tbodyEnterprise").html(html);
        //调用分页
        layui.use(['laypage', 'layer'], function() {
            var laypage = layui.laypage,
                layer = layui.layer;
            laypage.render({
                elem: 'enterpriseList',
                count: total,
                limit: dataObj.limit_enterprise,
                first: '首页',
                last: '尾页',
                layout: ['count', 'prev', 'page', 'next', 'limit', 'skip'],
                curr: dataObj.page_enterprise,
                theme: '#00A0E9',
                jump:function(obj,first){
                    if(!first) {
    　　　　　　　　　　　　//***第一次不执行,一定要记住,这个必须有,要不然就是死循环,哈哈
                        var curr = obj.curr;
　　　　　　　　　　　　　　//更改存储变量容器中的数据,是之随之更新数据
                        dataObj.page_enterprise = obj.curr;
                        dataObj.limit_enterprise= obj.limit;
　　　　　　　　　　　　　　//回调该展示数据的方法,数据展示
                        GetEnterprise(curr)
                    }
                }
            });
        });

    });
}