/**
 * Created by zhangbo on 2019/5/7.
 */

// 获取项目列表
var projectInit = function(){

    var options = "";

    function getProjectListInfo(){


        $.get("/project/get_project_list/",{},function (resp) {

            if (resp.status === 10200) {

                console.log(resp.data);

            }
        })
    }

    getProjectListInfo();


}
