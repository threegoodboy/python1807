/*
* @author : weber liu
* @version : v1.1
*/

var Validator = function(name)
{
  this.errorCss = "validatorError";
  this.formName = name;
  this.errMsg = new Array();

  /* *
  * 检查用户是否输入了内容
  *
  * @param :  controlId   表单元素的ID
  * @param :  msg         错误提示信息
  */
  this.required = function(controlId, msg)
  {
    var obj = document.forms[this.formName].elements[controlId];
	this.noError(obj);
    if (typeof(obj) == "undefined" || Utils.trim(obj.value) == "")
    {
	  this.hasError(obj);
      this.addErrorMsg(msg);
    }
  }
  ;

  /* *
  * 检查用户输入的是否为合法的邮件地址
  *
  * @param :  controlId   表单元素的ID
  * @param :  msg         错误提示信息
  * @param :  required    是否必须
  */
  this.isEmail = function(controlId, msg, required)
  {
    var obj = document.forms[this.formName].elements[controlId];
    obj.value = Utils.trim(obj.value);

	this.noError(obj);
    if ( ! required && obj.value == '')
    {
      return;
    }

    if ( ! Utils.isEmail(obj.value))
    {
	  this.hasError(obj);
      this.addErrorMsg(msg);
    }
  }

  /* *
  * 检查两个表单元素的值是否相等
  *
  * @param : fstControl   表单元素的ID
  * @param : sndControl   表单元素的ID
  * @param : msg         错误提示信息
  */
  this.eqaul = function(fstControl, sndControl, msg)
  {
    var fstObj = document.forms[this.formName].elements[fstControl];
    var sndObj = document.forms[this.formName].elements[sndControl];

	this.noError(fstObj);
	this.noError(sndObj);
    if (fstObj != null && sndObj != null)
    {
      if (fstObj.value == '' || fstObj.value != sndObj.value)
      {
		this.hasError(fstObj);
	    this.hasError(sndObj);
        this.addErrorMsg(msg);
      }
    }
  }

  /* *
  * 检查前一个表单元素是否大于后一个表单元素
  *
  * @param : fstControl   表单元素的ID
  * @param : sndControl   表单元素的ID
  * @param : msg                错误提示信息
  */
  this.gt = function(fstControl, sndControl, msg)
  {
    var fstObj = document.forms[this.formName].elements[fstControl];
    var sndObj = document.forms[this.formName].elements[sndControl];

	this.noError(sndObj);
	this.noError(fstObj);
    if (fstObj != null && sndObj != null) {
      if (Utils.isNumber(fstObj.value) && Utils.isNumber(sndObj.value)) {
        var v1 = parseFloat(fstObj.value) + 0;
        var v2 = parseFloat(sndObj.value) + 0;
      } else {
        var v1 = fstObj.value;
        var v2 = sndObj.value;
      }

      if (v1 <= v2){
		  this.hasError(sndObj);
		  this.hasError(fstObj);
		  this.addErrorMsg(msg);
	  }
    }
  }

  /* *
  * 检查输入的内容是否是一个数字
  *
  * @param :  controlId   表单元素的ID
  * @param :  msg         错误提示信息
  * @param :  required    是否必须
  */
  this.isNumber = function(controlId, msg, required)
  {
    var obj = document.forms[this.formName].elements[controlId];
    obj.value = Utils.trim(obj.value);

	this.noError(obj);
    if (obj.value == '' && ! required)
    {
      return;
    }
    else
    {
      if ( ! Utils.isNumber(obj.value))
      {
	    this.hasError(obj);
        this.addErrorMsg(msg);
      }
    }
  }

  /* *
  * 检查输入的内容是否是一个整数
  *
  * @param :  controlId   表单元素的ID
  * @param :  msg         错误提示信息
  * @param :  required    是否必须
  */
  this.isInt = function(controlId, msg, required)
  {

    if (document.forms[this.formName].elements[controlId])
    {
      var obj = document.forms[this.formName].elements[controlId];
    }
    else
    {
      return;    
    }

    obj.value = Utils.trim(obj.value);
	this.noError(obj);

    if (obj.value == '' && ! required)
    {
      return;
    }
    else
    {
      if ( ! Utils.isInt(obj.value)){
		  this.hasError(obj);
		  this.addErrorMsg(msg);
	  }
    }
  }

  /* *
  * 检查输入的内容是否是为空
  *
  * @param :  controlId   表单元素的ID
  * @param :  msg         错误提示信息
  * @param :  required    是否必须
  */
  this.isNullOption = function(controlId, msg)
  {
    var obj = document.forms[this.formName].elements[controlId];

    obj.value = Utils.trim(obj.value);
	this.noError(obj);

    if (obj.value > '0' )
    {
      return;
    }
    else
    {
	  this.hasError(obj);
      this.addErrorMsg(msg);
    }
  }

  /* *
  * 检查输入的内容是否是"2006-11-12 12:00:00"格式
  *
  * @param :  controlId   表单元素的ID
  * @param :  msg         错误提示信息
  * @param :  required    是否必须
  */
  this.isTime = function(controlId, msg, required)
  {
    var obj = document.forms[this.formName].elements[controlId];
    obj.value = Utils.trim(obj.value);

	this.noError(obj);
    if (obj.value == '' && ! required)
    {
      return;
    }
    else
    {
      if ( ! Utils.isTime(obj.value)){
		  this.hasError(obj);
		  this.addErrorMsg(msg);
	  }
    }
  }
  
  /* *
  * 检查前一个表单元素是否小于后一个表单元素(日期判断)
  *
  * @param : controlIdStart   表单元素的ID
  * @param : controlIdEnd     表单元素的ID
  * @param : msg              错误提示信息
  */
  this.islt = function(controlIdStart, controlIdEnd, msg)
  {
    var start = document.forms[this.formName].elements[controlIdStart];
    var end = document.forms[this.formName].elements[controlIdEnd];
    start.value = Utils.trim(start.value);
    end.value = Utils.trim(end.value);

	this.noError(start);
	this.noError(end);
    if(start.value <= end.value)
    {
      return;
    }
    else
    {
	  this.hasError(start);
	  this.hasError(end);
      this.addErrorMsg(msg);
    }
  }

  /* *
  * 检查指定的checkbox是否选定
  *
  * @param :  controlId   表单元素的name
  * @param :  msg         错误提示信息
  */
  this.requiredCheckbox = function(chk, msg)
  {
    var obj = document.forms[this.formName].elements[controlId];
    var checked = false;

	this.noError(obj);
    for (var i = 0; i < objects.length; i ++ )
    {
      if (objects[i].type.toLowerCase() != "checkbox") continue;
      if (objects[i].checked)
      {
        checked = true;
        break;
      }
    }

    if ( ! checked){
	    this.hasError(obj);
		this.addErrorMsg(msg);
	}
  }

  this.passed = function()
  {
    if (this.errMsg.length > 0)
    {
      var msg = "";
      for (i = 0; i < this.errMsg.length; i ++ )
      {
        msg += "> " + this.errMsg[i] + "\n<br/>";
      }
      Mix.alert(msg);
      return false;
    }
    else
    {
      return true;
    }
  }

  /* *
  * 增加一个错误信息
  *
  * @param :  str
  */
  this.addErrorMsg = function(str)
  {
    this.errMsg.push(str);
  }
  /* *
  * 错误时的处理
  *
  * @param :  str
  */
  this.hasError = function(obj)
  {
	if($(obj).attr('type')=="radio") $(obj).parent().addClass(this.errorCss);
    else $(obj).addClass(this.errorCss);
  }
  this.noError = function(obj)
  {
	if($(obj).attr('type')=="radio") $(obj).parent().removeClass(this.errorCss);
    else $(obj).removeClass(this.errorCss);
  }
}

/* $Id : utils.js 5052 2007-02-03 10:30:13Z weberliu $ */
var Browser = new Object();
Browser.isMozilla = (typeof document.implementation != 'undefined') && (typeof document.implementation.createDocument != 'undefined') && (typeof HTMLDocument != 'undefined');
Browser.isIE = window.ActiveXObject ? true : false;
Browser.isFirefox = (navigator.userAgent.toLowerCase().indexOf("firefox") != - 1);
Browser.isSafari = (navigator.userAgent.toLowerCase().indexOf("safari") != - 1);
Browser.isOpera = (navigator.userAgent.toLowerCase().indexOf("opera") != - 1);

var Utils = new Object();

Utils.htmlEncode = function(text)
{
  return text.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

Utils.trim = function( text )
{
  if (typeof(text) == "string")
  {
    return text.replace(/^\s*|\s*$/g, "");
  }
  else
  {
    return text;
  }
}

Utils.isEmpty = function( val )
{
  switch (typeof(val))
  {
    case 'string':
      return Utils.trim(val).length == 0 ? true : false;
      break;
    case 'number':
      return val == 0;
      break;
    case 'object':
      return val == null;
      break;
    case 'array':
      return val.length == 0;
      break;
    default:
      return true;
  }
}

Utils.isNumber = function(val)
{
  var reg = /^[\d|\.|,]+$/;
  return reg.test(val);
}

Utils.isInt = function(val)
{
  if (val == "")
  {
    return false;
  }
  var reg = /\D+/;
  return !reg.test(val);
}

Utils.isEmail = function( email )
{
  var reg1 = /([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)/;

  return reg1.test( email );
}

Utils.isTel = function ( tel )
{
  var reg = /^[\d|\-|\s|\_]+$/; //只允许使用数字-空格等

  return reg.test( tel );
}

Utils.fixEvent = function(e)
{
  var evt = (typeof e == "undefined") ? window.event : e;
  return evt;
}

Utils.srcElement = function(e)
{
  if (typeof e == "undefined") e = window.event;
  var src = document.all ? e.srcElement : e.target;

  return src;
}

Utils.isTime = function(val)
{
  var reg = /^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}$/;

  return reg.test(val);
}

Utils.x = function(e)
{ //当前鼠标X坐标
    return Browser.isIE?event.x + document.documentElement.scrollLeft - 2:e.pageX;
}

Utils.y = function(e)
{ //当前鼠标Y坐标
    return Browser.isIE?event.y + document.documentElement.scrollTop - 2:e.pageY;
}

Utils.request = function(url, item)
{
	var sValue=url.match(new RegExp("[\?\&]"+item+"=([^\&]*)(\&?)","i"));
	return sValue?sValue[1]:sValue;
}

Utils.$ = function(name)
{
    return document.getElementById(name);
}

function rowindex(tr)
{
  if (Browser.isIE)
  {
    return tr.rowIndex;
  }
  else
  {
    table = tr.parentNode.parentNode;
    for (i = 0; i < table.rows.length; i ++ )
    {
      if (table.rows[i] == tr)
      {
        return i;
      }
    }
  }
}

document.getCookie = function(sName)
{
  // cookies are separated by semicolons
  var aCookie = document.cookie.split("; ");
  for (var i=0; i < aCookie.length; i++)
  {
    // a name/value pair (a crumb) is separated by an equal sign
    var aCrumb = aCookie[i].split("=");
    if (sName == aCrumb[0])
      return decodeURIComponent(aCrumb[1]);
  }

  // a cookie with the requested name does not exist
  return null;
}

document.setCookie = function(sName, sValue, sExpires)
{
  var sCookie = sName + "=" + encodeURIComponent(sValue);
  if (sExpires != null)
  {
    sCookie += "; expires=" + sExpires;
  }

  document.cookie = sCookie;
}

document.removeCookie = function(sName,sValue)
{
  document.cookie = sName + "=; expires=Fri, 31 Dec 1999 23:59:59 GMT;";
}

function getPosition(o)
{
    var t = o.offsetTop;
    var l = o.offsetLeft;
    while(o = o.offsetParent)
    {
        t += o.offsetTop;
        l += o.offsetLeft;
    }
    var pos = {top:t,left:l};
    return pos;
}

function cleanWhitespace(element)
{
  var element = element;
  for (var i = 0; i < element.childNodes.length; i++) {
   var node = element.childNodes[i];
   if (node.nodeType == 3 && !/\S/.test(node.nodeValue))
     element.removeChild(node);
   }
}