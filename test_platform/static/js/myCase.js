/**
 * Created by zhangbo on 2019/5/7.
 */

// 创建下拉选项
function cmbAddOption(cmb,obj){

    console.log(obj);

    // 创建option标签元素
    var option = document.createElement("option");

    // 添加option到选项
    cmb.options.add(option);

    // 元素值
    option.innerHTML = obj.name;

    // 元素value值
    option.value = obj.id;

}

// 清除下拉选项
function clearOption(cmb){

    for(let i=0; i<= cmb.length+1; i++){

        cmb.options.remove(cmb[i]);

    }
}


// 获取项目列表
var projectInit = function(_cmbProject){

    var cmbProject = document.getElementById(_cmbProject);

    function getProjectListInfo(){

        $.get("/project/get_project_list/",{},function (resp) {

            if (resp.status === 10200) {

                console.log(resp.data);

                let dataList = resp.data;

                for(var i = 0; i < dataList.length; i++){

                    cmbAddOption(cmbProject,dataList[i]);

                }

            }
        })
    }

    // 调用getProjectListInfo
    getProjectListInfo();

}


// 获取某一个项目的模块列表
var ModuleInit = function(_cmbModule,pid){

    var cmbModule = document.getElementById(_cmbModule);

    function getModuleListInfo(){

        $.post("/module/get_module_list/",{"pid":pid},function (resp) {

            if (resp.status === 10200) {

                console.log(resp.data);

                let dataList = resp.data;

                clearOption(cmbModule);

                for(let i = 0; i < dataList.length; i++){

                    cmbAddOption(cmbModule,dataList[i]);

                }

                $("#module_name").selectpicker("refresh");

            }

            else {

                window.alert(resp.message);

            }
        })
    }

    // 调用getModuleListInfo
    getModuleListInfo();

}

