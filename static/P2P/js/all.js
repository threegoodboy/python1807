jQuery(function () {
// 首页下拉	 
    function slideNav(slidewper, slidebox) {
        $(slidewper).toggle(function () {
            $(this).find(slidebox).stop(true).slideDown(300);
        }, function () {
            $(this).find(slidebox).stop(true).slideUp(300);
        })
    };
    slideNav(".zxcf_nav_r", ".zxcf_perinfo");


// 排行榜切换
    function qiehuan(obj, objcur, boxone) {
        $(obj).click(function () {
            $(this).addClass(objcur).siblings().removeClass(objcur);
            var index = $(this).index();

            $(boxone).eq(index).show().siblings().hide();
        });
    }

    qiehuan(".block5_r_tit_em a", "brt_acur", ".rank_list");
//投资页切换 
    qiehuan(".product_tit span", "product_curspan", ".product_list");
    // borrow 切换
    qiehuan(".bor_detail_tit span", "bor_decurspan", ".bor_det_one");

// 项目列表切换
    function qiehuan2(obj, objcur, boxone) {
        $(obj).click(function () {
            $(this).addClass(objcur).siblings().removeClass(objcur);
            var index = $(this).index();
            if (index == 2) {
                $(boxone).eq(1).show().siblings().hide();
            } else {
                $(boxone).eq(index).show().siblings().hide();
            }
        });
    }

    qiehuan2(".block3_tit span", "block3_curspan", ".block3_prolist");
    // qiehuan2(".news_span","block3_curspan",".news_ul");


// invest页 筛选
    var aa;
    $(".invest_prochoose p a").click(function () {
        // $('.pagelink a')
        var a = $(this).parent().index();
        var b = $(this).index();
        $(this).addClass("inpro_cura").siblings().removeClass("inpro_cura");
        // $.get('/newapp/invests/1', {'a':a,b:b}, function (show_num) {
        //         alert(show_num)
        // })
        $.ajax({
            url: '/newapp/inv_ajax/',
            type: 'post',
            data: {'a': a, 'b': b},
            // async:false,
            success: function (data) {
                // alert(data['aa'])
                var html1 = ""
                var html = ""
                for (var i = 0; i < data['aa'].length; i++) {
                    var aaa = data['aa'][i]
                    html += "<div class=\"product_list mt20\"><div class=\"prolist_one prolist_one_bl01 mt20\"><h2 class=\"prolist_one_tit\"><span>" + aaa[0] + "</span>" + aaa[1] + "</h2><ul class=\"prolist_one_ul clearfix\"><li>年华收益：<strong>" + aaa[2] + "%</strong><br>还款方式：按月付息，到期还本</li><li>剩余期限：<i>" + aaa[3] + "</i>天<br>保障机构：" + aaa[4] + "</li><li class=\"prolist_press\">募集金额：<strong>" + aaa[5] + "</strong> 元 <br>认购进度：<span class=\"ui-progressbar-mid ui-progressbar-mid-100\">" + aaa[6] + "%</span></li><li class=\"prolist_btn\"><a onclick='detial("+aaa[8]+")' class=\"pro_btn\">" + aaa[7] + "</a></li></ul></div></div>"
                }
                $("#inv").html(html);
                for (var n = 0; n < data['page_range'].length; n++) {
                    var bbb = data['page_range'][n]
                    html1 += "<a onclick='page_a_callback("+bbb+")'>" + bbb + "</a>"
                }
                $("#page").html(html1);
            }
        })

    });

    $("#cve").click(function () {
        $.ajax({
            url: '/newapp/shouup/',
            type: 'post',
            data: {'a': 'aaa'},
            success: function (data) {
                var html1 = ""
                var html = ""
                for (var i = 0; i < data['aa'].length; i++) {
                    var aaa = data['aa'][i]
                    html += "<div class=\"product_list mt20\"><div class=\"prolist_one prolist_one_bl01 mt20\"><h2 class=\"prolist_one_tit\"><span>" + aaa[0] + "</span>" + aaa[1] + "</h2><ul class=\"prolist_one_ul clearfix\"><li>年华收益：<strong>" + aaa[2] + "%</strong><br>还款方式：按月付息，到期还本</li><li>剩余期限：<i>" + aaa[3] + "</i>天<br>保障机构：" + aaa[4] + "</li><li class=\"prolist_press\">募集金额：<strong>" + aaa[5] + "</strong> 元 <br>认购进度：<span class=\"ui-progressbar-mid ui-progressbar-mid-100\">" + aaa[6] + "%</span></li><li class=\"prolist_btn\"><a onclick='detial("+aaa[8]+")'class=\"pro_btn\">" + aaa[7] + "</a></li></ul></div></div>"
                }
                $("#inv").html(html);


            }
        })

    });

    // function page_a_callback() {
    //     alert('jjjjjjjjjjjjjjj')
    //     var page = $(this).index()
    //     $.ajax({
    //         url: '/newapp/page/',
    //         type: 'post',
    //         data: {'ind': page},
    //         success: function (data) {
    //             alert('xxxxxxxxxxx')
    //             for (var i = 0; i < data['aa'].length; i++) {
    //                 var aaa = data['aa'][i]
    //                 html += "<div class=\"product_list mt20\"><div class=\"prolist_one prolist_one_bl01 mt20\"><h2 class=\"prolist_one_tit\"><span>" + aaa[0] + "</span>" + aaa[1] + "</h2><ul class=\"prolist_one_ul clearfix\"><li>年华收益：<strong>" + aaa[2] + "%</strong><br>还款方式：按月付息，到期还本</li><li>剩余期限：<i>" + aaa[3] + "</i>天<br>保障机构：" + aaa[4] + "</li><li class=\"prolist_press\">募集金额：<strong>" + aaa[5] + "</strong> 元 <br>认购进度：<span class=\"ui-progressbar-mid ui-progressbar-mid-100\">" + aaa[6] + "%</span></li><li class=\"prolist_btn\"><a href=\"detail.html\" class=\"pro_btn\">" + aaa[7] + "</a></li></ul></div></div>"
    //             }
    //             $("#inv").html(html);
    //         }
    //     })
    //
    // }

    $("#page a").click(page_a_callback);

    $("#tim").click(function () {

        $.ajax({
            url: '/newapp/timeup/',
            type: 'post',
            data: {'a': 'aaa'},
            success: function (data) {
                // alert(data['aa'])
                var html = ""
                for (var i = 0; i < data['aa'].length; i++) {
                    var aaa = data['aa'][i]
                    html += "<div class=\"product_list mt20\"><div class=\"prolist_one prolist_one_bl01 mt20\"><h2 class=\"prolist_one_tit\"><span>" + aaa[0] + "</span>" + aaa[1] + "</h2><ul class=\"prolist_one_ul clearfix\"><li>年华收益：<strong>" + aaa[2] + "%</strong><br>还款方式：按月付息，到期还本</li><li>剩余期限：<i>" + aaa[3] + "</i>天<br>保障机构：" + aaa[4] + "</li><li class=\"prolist_press\">募集金额：<strong>" + aaa[5] + "</strong> 元 <br>认购进度：<span class=\"ui-progressbar-mid ui-progressbar-mid-100\">" + aaa[6] + "%</span></li><li class=\"prolist_btn\"><a onclick='detial("+aaa[8]+")' class=\"pro_btn\">" + aaa[7] + "</a></li></ul></div></div>"
                }
                $("#inv").html(html);
            }
        })

    });
    $("#dat").click(function () {

        $.ajax({
            url: '/newapp/dateup/',
            type: 'post',
            data: {'a': 'aaa'},
            success: function (data) {
                // alert(data['aa'])
                var html = ""
                for (var i = 0; i < data['aa'].length; i++) {
                    var aaa = data['aa'][i]
                    html += "<div class=\"product_list mt20\"><div class=\"prolist_one prolist_one_bl01 mt20\"><h2 class=\"prolist_one_tit\"><span>" + aaa[0] + "</span>" + aaa[1] + "</h2><ul class=\"prolist_one_ul clearfix\"><li>年华收益：<strong>" + aaa[2] + "%</strong><br>还款方式：按月付息，到期还本</li><li>剩余期限：<i>" + aaa[3] + "</i>天<br>保障机构：" + aaa[4] + "</li><li class=\"prolist_press\">募集金额：<strong>" + aaa[5] + "</strong> 元 <br>认购进度：<span class=\"ui-progressbar-mid ui-progressbar-mid-100\">" + aaa[6] + "%</span></li><li class=\"prolist_btn\"><a onclick='detial("+aaa[8]+")' class=\"pro_btn\">" + aaa[7] + "</a></li></ul></div></div>"
                }
                $("#inv").html(html);
            }
        })

    });

// problem页 切换
    $(".hc_zjwt_one h3").click(function () {

        if ($(this).hasClass("show")) {
            $(this).parents(".hc_zjwt_one").find(".hc_answer").hide().end().find(this).removeClass("show");
        } else {
            $(".hc_answer").hide().parents(".hc_zjwt_one").find(".hc_zjwt_one h3").removeClass("show");
            $(this).parents(".hc_zjwt_one").find(".hc_answer").show().end().find(this).addClass("show");
        }

    });


// noticlist页 
    $(".notic_secl_ul li").click(function () {

        $(this).addClass("notic_curli").siblings().removeClass("notic_curli");
    });


});
