/**
 * Created by zhangbo on 2019/5/7.
 */

// 获取项目列表
var projectInit = function(_cmbProject){

    var cmbProject = document.getElementById(_cmbProject);

    var options = "";

    // 创建下拉选项
    function cmbAddOption(cmb,project_obj){

        console.log(project_obj);

        // 创建option标签元素
        var option = document.createElement("option");

        // 添加option到选项
        cmb.options.add(option);

        // 元素值
        option.innerHTML = project_obj.name;

        // 元素value值
        option.value = project_obj.id;

    }

    function getProjectListInfo(){

        $.get("/project/get_project_list/",{},function (resp) {

            if (resp.status === 10200) {

                console.log(resp.data);

                let dataList = resp.data;

                for(var i = 0; i < dataList.length; i++){

                    cmbAddOption(cmbProject,dataList[i]);

                }

                // cmbSelect(cmbProject,defaultProject);

            }
        })
    }

    getProjectListInfo();


}
