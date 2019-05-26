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

};


// 清除下拉选项
function clearOption(cmb){

    for(let i=0; i<= cmb.length+1; i++){

        cmb.options.remove(cmb[i]);

    }
};


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

};


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

};


// 获取下拉框模块列表所有option的list数据
var SelectModule = function(mid){

	let options2 = document.querySelectorAll("#module_name > option");

	for (let i = 0; i < options2.length; i++){

		let v2 = options2[i].value;

		if (v2 == mid){

			options2[i].selected = true;

			let text = options2[i].text;

			document.querySelectorAll(".filter-option-inner-inner")[1].innerText = text;

		}
	}
};


// 获取用例信息
var TestCaseInit = function() {

    // 获取当前url地址
    var url = document.location;

    console.log("url",url.pathname.split("/")[3]);

    var cid = url.pathname.split("/")[3];

    $.post("/testcase/get_case_info",
        {
            cid:cid
        },
        function(resp,status) {

            console.log("返回的结果", resp.data);

            // 请求URL
            document.querySelector("#req_url").value = resp.data.url;

            // 用例名称
            document.getElementById("case_name").value = resp.data.name;

            // 请求方法
            if (resp.data.method == 1) {

                document.querySelector("#get").setAttribute("checked", "");
            }

            else if (resp.data.method == 2) {

                document.querySelector("#post").setAttribute("checked", "");

            }

            else if (resp.data.method == 3) {

                document.querySelector("#put").setAttribute("checked", "");

            }

            else if (resp.data.method == 4) {

                document.querySelector("#delete").setAttribute("checked", "");

            }

            // 请求头
            document.getElementById("header").value = resp.data.header;

            // 请求类型
            if (resp.data.parameter_type == 1) {

                document.querySelector("#form").setAttribute("checked", "");
            }

            else if (resp.data.parameter_type == 2) {

                document.querySelector("#json").setAttribute("checked", "");

            }

            // 请求参数
            document.getElementById("req_parameter").value = resp.data.parameter_body;

            // 断言类型
            if (resp.data.assert_type == 1) {

                document.querySelector("#contains").setAttribute("checked", "");
            }

            else if (resp.data.assert_type == 2) {

                document.querySelector("#mathches").setAttribute("checked", "");

            }

            // 断言文本
            document.getElementById("assert").value = resp.data.assert_text;

            // 获取下拉框项目列表所有option的list数据
            let options = document.querySelectorAll("#project_name > option");

            for (let i = 0; i < options.length; i++) {

                // 获取下拉框列表第几条option数据value值
                let v = options[i].value;

                if (v == resp.data.project_id) {

                    // 获取当前下拉框第几条option被选中
                    options[i].selected = true;

                    // 获取下拉框列表第几条option数据text值
                    let text = options[i].text;

                    // 更改获取下拉框列表选中第几条option类的text值
                    document.querySelectorAll(".filter-option-inner-inner")[0].innerText = text;
                }
            }

            //ModuleInit=("module_name",resp.data.project_id);

            //SelectModule(resp.data.module_id);

        }
    )

};






















