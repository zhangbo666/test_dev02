/**
 * Created by zhangbo on 19/6/11.
 */

var caseTreeInit = function(){

   var zTreeObj;

   // zTree 的参数配置，深入使用请参考 API 文档（setting 配置详解）
   var setting = {

       check: {

           enable:true,
           chkStyle: 'checkbox'

       }
   };

   // zTree 的数据属性，深入使用请参考 API 文档（zTreeNode 节点数据详解）
   //var zNodes = [
   //    {
   //        name:"项目1",
   //        open:true,
   //        children: [
   //            {
   //                name:"模块AAA",
   //                open:true,
   //                children: [
   //                    {
   //                        name:"1"
   //                    },
   //                    {
   //                        name:"2"
   //                    }
   //                ]
   //            },
   //
   //            {
   //                name:"模块BBB"
   //            }
   //        ]
   //    },
   //    {
   //        name:"项目2",
   //        open:true,
   //        children: [
   //            {
   //                name:"模块001",
   //                open:true,
   //                children:
   //                        [
   //                            {name:"3"}
   //                        ]
   //
   //            },
   //            {
   //                name:"模块002"
   //            }
   //
   //
   //        ]
   //    }
   //];

   $(document).ready(function (){

       $.get("/testtask/get_case_tree/",{},

       function (resp) {

           if (resp.status === 10200){

               //window.alert("创建任务成功！");

               var zNodes = resp.data;

               zTreeObj = $.fn.zTree.init($("#treeDemo"), setting, zNodes);

               zTreeObj.expandAll(true);

           }
       })
   });

};