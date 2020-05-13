var CommonJS = {
    RemoveLastsingleQuote(char) {
      try {
        if(typeof(char) == "string"){
          var char = char.trim();
          var lastchar = char.charAt(char.length - 1)
          if (lastchar == "'" || lastchar == ",")
            return char.substring(0, char.length - 1).replace(/[?:]/g, "");
          else
            return char.replace(/[?:]/g, "")
        }
      } catch (error) {
        console.log(error);
        return ""
      }
    },
    RemoveNullValue: function (val) {
      if (val != undefined && val != null && val != "null")
        return val;
      else
        return "";
    },
    RemoveNullValuewithzero: function (val) {
      if (val != undefined && val != null && val != "null" && val != "")
        return val;
      else
        return 0;
    },
    RemoveNullValuewithQuotes: function (val) {
      if (val != undefined && val != null && val != "null" && val != "")
        return val;
      else
        return '""';
    },
};