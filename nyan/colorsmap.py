# Adapted from
# https://github.com/klange/nyancat/blob/master/src/nyancat.c

def getColors(kind=1):
    if kind not in [1,2,3,4,5,6,7]:
        raise Exception("Wrong color map kind.  (%r not 1-7)" % kind)
    always_escape = False
    output = "  "
    colors = {}

    if kind == 1:
        colors[',']  = "\033[48;5;17m";  
        colors['.']  = "\033[48;5;231m"; 
        colors['\''] = "\033[48;5;16m";  
        colors['@']  = "\033[48;5;230m"; 
        colors['$']  = "\033[48;5;175m"; 
        colors['-']  = "\033[48;5;162m"; 
        colors['>']  = "\033[48;5;196m"; 
        colors['&']  = "\033[48;5;214m"; 
        colors['+']  = "\033[48;5;226m"; 
        colors['#']  = "\033[48;5;118m"; 
        colors['=']  = "\033[48;5;33m";  
        colors[';']  = "\033[48;5;19m";  
        colors['*']  = "\033[48;5;240m"; 
        colors['%']  = "\033[48;5;175m"; 

    if kind == 2:
        colors[',']  = "\033[104m";      
        colors['.']  = "\033[107m";      
        colors['\''] = "\033[40m";       
        colors['@']  = "\033[47m";       
        colors['$']  = "\033[105m";      
        colors['-']  = "\033[101m";      
        colors['>']  = "\033[101m";      
        colors['&']  = "\033[43m";       
        colors['+']  = "\033[103m";      
        colors['#']  = "\033[102m";      
        colors['=']  = "\033[104m";      
        colors[';']  = "\033[44m";       
        colors['*']  = "\033[100m";      
        colors['%']  = "\033[105m";      

    if kind == 3:
        colors[',']  = "\033[25;44m";    
        colors['.']  = "\033[5;47m";     
        colors['\''] = "\033[25;40m";    
        colors['@']  = "\033[5;47m";     
        colors['$']  = "\033[5;45m";     
        colors['-']  = "\033[5;41m";     
        colors['>']  = "\033[5;41m";     
        colors['&']  = "\033[25;43m";    
        colors['+']  = "\033[5;43m";     
        colors['#']  = "\033[5;42m";     
        colors['=']  = "\033[25;44m";    
        colors[';']  = "\033[5;44m";     
        colors['*']  = "\033[5;40m";     
        colors['%']  = "\033[5;45m";     

    if kind == 4:
        colors[',']  = "\033[0;34;44m";  
        colors['.']  = "\033[1;37;47m";  
        colors['\''] = "\033[0;30;40m";  
        colors['@']  = "\033[1;37;47m";  
        colors['$']  = "\033[1;35;45m";  
        colors['-']  = "\033[1;31;41m";  
        colors['>']  = "\033[1;31;41m";  
        colors['&']  = "\033[0;33;43m";  
        colors['+']  = "\033[1;33;43m";  
        colors['#']  = "\033[1;32;42m";  
        colors['=']  = "\033[1;34;44m";  
        colors[';']  = "\033[0;34;44m";  
        colors['*']  = "\033[1;30;40m";  
        colors['%']  = "\033[1;35;45m";  
        output = u"\u2588"+u"\u2588"

    if kind == 5:
        colors[',']  = "\033[0;34;44m";  
        colors['.']  = "\033[1;37;47m";  
        colors['\''] = "\033[0;30;40m";  
        colors['@']  = "\033[1;37;47m";  
        colors['$']  = "\033[1;35;45m";  
        colors['-']  = "\033[1;31;41m";  
        colors['>']  = "\033[1;31;41m";  
        colors['&']  = "\033[0;33;43m";  
        colors['+']  = "\033[1;33;43m";  
        colors['#']  = "\033[1;32;42m";  
        colors['=']  = "\033[1;34;44m";  
        colors[';']  = "\033[0;34;44m";  
        colors['*']  = "\033[1;30;40m";  
        colors['%']  = "\033[1;35;45m";  
        output = "\333\333";

    if kind == 6:
        colors[',']  = "::";             
        colors['.']  = "@@";             
        colors['\''] = "  ";             
        colors['@']  = "##";             
        colors['$']  = "??";             
        colors['-']  = "<>";             
        colors['>']  = "##";             
        colors['&']  = "==";             
        colors['+']  = "--";             
        colors['#']  = "++";             
        colors['=']  = "~~";             
        colors[';']  = "$$";             
        colors['*']  = ";;";             
        colors['%']  = "()";             
        always_escape = True

    if kind == 7:
        colors[',']  = ".";             
        colors['.']  = "@";             
        colors['\''] = " ";             
        colors['@']  = "#";             
        colors['$']  = "?";             
        colors['-']  = "O";             
        colors['>']  = "#";             
        colors['&']  = "=";             
        colors['+']  = "-";             
        colors['#']  = "+";             
        colors['=']  = "~";             
        colors[';']  = "$";             
        colors['*']  = ";";             
        colors['%']  = "o";             
        always_escape = True

    return (colors, output, always_escape)
