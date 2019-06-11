/** *************index JS*********************
	
    TABLE OF CONTENTS
	---------------------------
	1.submitConfirm function
    2.initHttp function
    3.initInputs function
 ** ***************************************/

/***** submitConfirm function start *****/
var submitConfirm = function() {
    //表单提交验证
    $('#submitForm').bootstrapValidator({
        //        live: 'disabled',
        message: 'This value is not valid',
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            long: {
                validators: {
                    notEmpty: {
                        message: ' '
                    },
                    regexp: {
                        regexp: /^-?([1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0|-?[1-9]\d*)$/,
                        message: ' '
                    }
                }
            },
            lat: {
                validators: {
                    notEmpty: {
                        message: ' '
                    },
                    regexp: {
                        regexp: /^-?([1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0|-?[1-9]\d*)$/,
                        message: ' '
                    }
                }
            },
            day: {
                validators: {
                    notEmpty: {
                        message: ' '
                    },
                    regexp: {
                        regexp: /^([1-2][0-9]|[0][1-9]|[3][0-1])$/,
                        message: ' '
                    }
                }
            },
            month: {
                validators: {
                    notEmpty: {
                        message: ' '
                    },
                    regexp: {
                        regexp: /^([1][0-2]|[0][1-9])$/,
                        message: ' '
                    }
                }
            },
            year: {
                validators: {
                    notEmpty: {
                        message: ' '
                    },
                    regexp: {
                        regexp: /^([0-9][0-9][0-9][0-9])$/,
                        message: ' '
                    }
                }
            },
            time: {
                validators: {
                    notEmpty: {
                        message: ' '
                    },
                    regexp: {
                        regexp: /^(([0-1][0-9]|[2][0-3])([0-5][0-9]))$/,
                        message: '1330 -> 13:30'
                    }
                }
            },
            nbv: {
                validators: {
                    notEmpty: {
                        message: ' '
                    },
                    regexp: {
                        regexp: /^([1-9]\d*|0)$/,
                        message: ' '
                    }
                }
            },
            lartpc: {
                validators: {
                    notEmpty: {
                        message: ' '
                    },
                    regexp: {
                        regexp: /^([1-9]\d*|0)$/,
                        message: ' '
                    }
                }
            },
            larrout: {
                validators: {
                    notEmpty: {
                        message: ' '
                    },
                    regexp: {
                        regexp: /^([1-9]\d*|0)$/,
                        message: ' '
                    }
                }
            },
        },
    });
};
/***** submitConfirm function end *****/

/***** initHttp function start *****/
var initHttp = function() {
    $("#deaths").click(function() {
        var options = {
            // url: "http://fr.hshsilver.com/deaths", //同action 
            url: "http://fr.hshsilver.com/deaths",
            type: 'post',
            beforeSend: function(xhr) { //请求之前
                var index = layer.load(1, {
                    shade: [0.5, '#000'] //0.5透明度的黑色背景
                });
            },
            success: function(data) {
                data = $.parseJSON(data);
                localStorage.setItem("myPrediction", JSON.stringify(data));
                localStorage.setItem("myUpdateLat", ($("#lat").val() * 100000) / 1);
                localStorage.setItem("myUpdateLng", ($("#long").val() * 100000) / 1);
                document.getElementById('result').contentWindow.location.reload(true);
                $('#upload').css('display', 'none');
                $("#result").attr("src", 'radar-custom.html');
                $("#result").attr("height", '500px');
            },

            complete: function(xhr) { //请求完成
                layer.closeAll('loading');
            },

            error: function(xhr, status, msg) {
                //alert("状态码"+status+"; "+msg)
                $('#deal-result').css('display', 'none');
                layer.msg('上传失败...');

            }
        };
        var bootstrapValidator = $("#submitForm").data('bootstrapValidator');
        bootstrapValidator.validate();
        if (bootstrapValidator.isValid())
            $("#submitForm").ajaxSubmit(options);
        else {
            alert("请检查各输入项是否符合要求！");
            return;
        }

    });
    $("#probability").click(function() {
        var options = {
            // url: "http://fr.hshsilver.com/probability", //同action 
            url: "http://fr.hshsilver.com/probability",
            type: 'post',
            beforeSend: function(xhr) { //请求之前
                var index = layer.load(1, {
                    shade: [0.5, '#000'] //0.5透明度的黑色背景
                });
            },
            success: function(data) {
                console.log($.parseJSON(data))
            },

            complete: function(xhr) { //请求完成
                layer.closeAll('loading');
            },

            error: function(xhr, status, msg) {
                //alert("状态码"+status+"; "+msg)
                $('#deal-result').css('display', 'none');
                layer.msg('上传失败...');

            }
        };
        var bootstrapValidator = $("#submitForm").data('bootstrapValidator');
        bootstrapValidator.validate();
        if (bootstrapValidator.isValid())
            $("#submitForm").ajaxSubmit(options);
        else {
            alert("请检查各输入项是否符合要求！");
            return;
        }

    });
};

var initInputs = function() {
    function initLocation() {
        if (navigator.geolocation) {
            //判断是否有这个对象
            navigator.geolocation.getCurrentPosition(function(pos) {
                //console.log("经度：" + pos.coords.longitude + "纬度：" + pos.coords.latitude)
                $("#long").val(pos.coords.longitude);
                $("#lat").val(pos.coords.latitude);
            })
        } else {
            console.log("当前系统不支持GPS API")
        }
    }

    function initTime() {
        var myDate = new Date();
        var day = String(myDate.getDate()).padStart(2, '0');
        var month = String(myDate.getMonth() + 1).padStart(2, '0');
        var year = String(myDate.getFullYear()).padStart(4, '0');
        var hour = String(myDate.getHours()).padStart(2, '0');
        var mintue = String(myDate.getMinutes()).padStart(2, '0');
        // console.log(day, month, year, hour, mintue)
        $("#day").val(day);
        $("#month").val(month);
        $("#year").val(year);
        $("#time").val(hour + mintue);
    }
    initLocation();
    initTime();
}



/***** initHttp function end *****/
initHttp();
submitConfirm();
initInputs();