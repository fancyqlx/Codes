bool isMatch(char* s, char* p) {
    if (!*s && !*p) return true;
    else if(!*p) return false;
    if (*(p+1) == '*'){
        return isMatch(s,p+2) || (*s && (*s == *p || *p == '.') && isMatch(s+1,p));
    }
    else if(*s && (*s == *p || *p == '.')){
        return isMatch(s+1,p+1);
    }
    else{
        return false;
    }
}
