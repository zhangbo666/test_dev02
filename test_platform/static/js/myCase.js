/**
 * Created by zhangbo on 2019/5/7.
 */

// 获取项目列表
var projectInit = function(_cmbProject){

    var cmbProject = document.getElementById(_cmbProject);

    var options = "";

    // 创建下拉选项
    function cmbAddOption(cmb,str){

        console.log(str);

        var option = document.createElement("option");

        cmb.options.add(option);

        option.innerHTML = str;

        option.value = str;

        // option.obj = obj;


    }

    function getProjectListInfo(){

        $.get("/project/get_project_list/",{},function (resp) {

            if (resp.status === 10200) {

                console.log(resp.data);

                let dataList = resp.data;

                for(var i = 0; i < dataList.length; i++){

                    cmbAddOption(cmbProject,dataList[i],dataList[i]);

                }
            }
        })
    }

    getProjectListInfo();


}
