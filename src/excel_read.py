import xlrd  
import json  
import codecs  
import os  

#把excel表格中指定sheet转为json  
def read_excel(file_path):  
    #打开excel文件  
    SHEETS = []
    if get_data(file_path) is not None:  
        book = get_data(file_path)  
        #抓取所有sheet页的名称  
        worksheets = book.sheets()  
        print ("该Excel包含的表单列表为：\n", book.sheet_names()  )

        for sheet in worksheets:  
            print ('%s,%s' %(worksheets.index(sheet),sheet.name))  
            
            row_0 = sheet.row(0)     #第一行是表单标题  
            nrows=sheet.nrows       #行号  
            ncols=sheet.ncols       #列号  
            
            result={}   #定义json对象  
            result["title"]=file_path   #表单标题  
            result["rows"]=nrows        #行号  
            result["children"]=[]      #每一行作为数组的一项  
            
            for i in range(nrows):  
                if i==0:  
                    continue  
                record={}  
            
                for j in range(ncols):  
                    #获取当前列中文标题  
                    title_de=str(row_0[j])
                    # title_cn= str(title_de.split("'")[1]).strip()
                    #获取单元格的值  
                    if( title_de.strip() != "") :
                        record[title_de]=str(sheet.row_values(i)[j]).strip()#.replace("-","_")
                
                result["children"].append(record)  
            SHEETS.append(result)
            # json_data=json.dumps(result,indent= 4,sort_keys=True).encode('utf-8').decode('unicode_escape')      
    return SHEETS #json_data

# 获取excel数据源  
def get_data(file_path):  
    try:  
        data = xlrd.open_workbook(file_path)  
        return data  
    except Exception:  
        return None  
  
def save_file(file_path,file_name,data):  
    output = codecs.open(file_path+"/"+file_name+".json",'w',"utf-8")  
    output.write(data)  
    output.close()  


if __name__ == '__main__':  
    data = read_excel('sample.xls')  
    print ( len(data) ) 

