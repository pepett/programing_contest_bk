import re

class Utils:
    @staticmethod
    def sharp( text ):
        index = text.split( '#' )
        result = []
        index.pop( 0 )
        for t in index:
            tmp = t.split()
            result.append( tmp[ 0 ] )
        
        return result
    
    @staticmethod
    def del_duplicate( arr, is_rough ):
        ver_arr = arr
        result = []
        num = []
        for i in range( len( arr ) ):
            flg = True
            text = ver_arr[ i ]
            for j in range( len( result ) ):
                if text == result[ j ]:
                    flg = False
                    break
            if flg:
                result.append( text )
        return result

    @staticmethod
    def truncate_string(text, max_length):
        if len(text) <= max_length:
            return text
        else:
            return text[:max_length] + "..."