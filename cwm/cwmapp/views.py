from django.shortcuts import render
from django.shortcuts import redirect
from lib.spotify_conect import SPOTIFY
from lib.utils import Utils
from cwmapp.models import User, Comment

# Create your views here.
def top( request ):
    #例ここから 
    #tmp = Utils.sharp( "unti unti #aaaa \n un#ti #bbb jsflkdsj" )
    #for counter in range( len( tmp ) ):
    #    print( tmp[ counter ] )
    #例ここまで
    return render( request, 'cwm/top.html' )

def login( request ):
    return render( request, 'cwm/login.html' )

def register( request ):
    return render( request, 'cwm/register.html' )

def setting( request ):
        
        Userdata = User.objects.filter( user_name = 'morikin' , user_mail = 'k228021@kccollege.ac.jp')

        max_length = 13

        lz_uri = 'spotify:artist:3wvCMqwyJachksGLF0kjMJ'
        
        results = SPOTIFY.artist_top_tracks(lz_uri)
        final_result=results['tracks']

        lz_uri2 = 'spotify:artist:5Vo1hnCRmCM6M4thZCInCj'
        results2 = SPOTIFY.artist_top_tracks(lz_uri2)
        final_result2=results2['tracks']

        j = 0
        for i in final_result:
            final_result[j]['name'] = Utils.truncate_string(i['name'],max_length)
            final_result[j]['artists'][0]['name'] = Utils.truncate_string(i['artists'][0]['name'],max_length)
            j = j + 1

        j = 0
        for i in final_result2:
            final_result2[j]['name'] = Utils.truncate_string(i['name'],max_length)
            final_result2[j]['artists'][0]['name'] = Utils.truncate_string(i['artists'][0]['name'],max_length)
            j = j + 1

        return render(request,'cwm/setting.html',{"results":final_result,"results2":final_result2, "data":Userdata})


def result( request ):
    if not request.GET[ 'search-music' ]:
        return redirect( 'search' )
    results = SPOTIFY.search( request.GET['search-music'], limit=10, offset=0, type='track', market=None )
    ret = {
        'results': results,
        'word': request.GET[ 'search-music' ],
    }
    return render( request, 'cwm/result.html', ret  )

def index( request ):
        
        max_length = 13

        lz_uri = 'spotify:artist:3wvCMqwyJachksGLF0kjMJ'
        
        results = SPOTIFY.artist_top_tracks(lz_uri)
        final_result=results['tracks']

        lz_uri2 = 'spotify:artist:1snhtMLeb2DYoMOcVbb8iB'
        results2 = SPOTIFY.artist_top_tracks(lz_uri2)
        final_result2=results2['tracks']

        lz_uri3 = 'spotify:artist:5Vo1hnCRmCM6M4thZCInCj'
        results3 = SPOTIFY.artist_top_tracks(lz_uri3)
        final_result3=results3['tracks']

        j = 0
        for i in final_result:
            final_result[j]['name'] = Utils.truncate_string(i['name'],max_length)
            final_result[j]['artists'][0]['name'] = Utils.truncate_string(i['artists'][0]['name'],max_length)
            j = j + 1

        j = 0
        for i in final_result2:
            final_result2[j]['name'] = Utils.truncate_string(i['name'],max_length)
            final_result2[j]['artists'][0]['name'] = Utils.truncate_string(i['artists'][0]['name'],max_length)
#            print( i[ 'id' ] )//これをデータベースに入れる
            j = j + 1

        j = 0
        for i in final_result3:
            final_result3[j]['name'] = Utils.truncate_string(i['name'],max_length)
            final_result3[j]['artists'][0]['name'] = Utils.truncate_string(i['artists'][0]['name'],max_length)
            j = j + 1

        for tracks in final_result:
            return render(request,'cwm/index.html',{"results":final_result,"results2":final_result2,"results3":final_result3})

def music( request, idn ):#次回やることは、タグをどのコメントでも表示する,( コメントの複数表示 ) & エラー処理
    track_result = SPOTIFY.track( idn, market=None )
    comments = []
    tags = []
    users = []
    content = {
        'track_result': track_result,
        'comments': comments,
        'tags': tags,
        'users': users,
    }
    if Comment.objects.filter( comment_music_id=idn ).exists():
        comments = Comment.objects.filter( comment_music_id=idn )
        for i in range( comments.count() ):
            users.append( User.objects.get( user_mail=comments[ i ].comment_user_mail ) )#一つしかとってきてない
            tags.extend( Utils.sharp( comments[ i ].comment_text ) )
        tags = Utils.del_duplicate( tags, False )
        print( vars( comments[ 0 ] ) )
        
        content[ 'tags' ] = tags
        content[ 'comments' ] = comments
        content[ 'users' ] = users
    return render( request, 'cwm/music.html', content )

def user( request ):
    db = User.objects.all()
    data = {
        'db': db,
    }
    return render( request, 'cwm/user.html', data )

def search( request ):
    #if len( request.GET[ 'search-music' ] ) != 0:
    return render( request, 'cwm/search.html')