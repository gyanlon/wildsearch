<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=unicode">
    <style type="text/css"> 
        .title {color:#ddd} 
        .line {
            border-bottom:medium solid #aaa;
            border-width: 0 0 1 0; 
            padding-bottom: 5px;
            margin-bottom: 5px;
        }
    </style>
</head>
<form action="/search" method="post">
    <input name='querystr' type="text" maxlength="255" style="height:34;width:540"/ value="{{querystr}}">
    <input value="查查看" type="submit" style="height:34;width:100;background:#ddd;font-size:16"/>
</form>

% import re
% module = re.compile("\"text:'(.*?)'\"")
% for record in records:
<div class='line'>
    {{!record}}
</div>    
% end

</html>