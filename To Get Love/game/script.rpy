# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"

image bg blck = "images/blck.png"

# Deklarasikan karakter yang digunakan di game.
define e = Character('Nana' 'Miko', color="#c8ffc8")

# Game dimulai disini.
label start:
    scene kelas2
    play music "audio/In Dreamland background music.mp3"
    with fade
    play sound "Sound Effects - School bell (HD) (320).mp3" volume 2.0
    pause 1.0
    play sound "typing.mp3" volume 2.5
    "Bel sekolah berbuyi, siswa-siswi baru segera masuk ke kelas masing masing"

    with fade
    play sound "typing.mp3" volume 2.5
    "Waktunya siswa-siswi memperkenalkan diri"

    show miko senang at left
    play sound "typing.mp3" fadeout 3.0 volume 2.5
    play sound "<from 1>download (33).wav"
    "Miko" "Halo semuanya, namaku Miko"
    hide miko senang

    show nana bahagia at left
    play sound "<from 1>suara nana 1.wav"
    "Nana" "Halo semuanya, namaku Nana"


    with fade
    scene kelas2
    play sound "typing.mp3" volume 2.5
    "saat semua telah memperkenalkan diri, kelas berjalan seperti biasa"

    play sound "Crowd Talking Sound Effect.mp3" volume 1.5
    pause 5
    play sound "Sound Effects - School bell (HD) (320).mp3"

    with fade
    play sound "typing.mp3" volume 2.5
    "bel sekolah berbunyi tanda perpulangan sekolah"
    play sound "typing.mp3" volume 2.5
    "tiba tiba Nana mendekat menghampiri"
    with fade

label node2:
    scene hallway
    show nana terkejut at left
    play sound "typing.mp3" fadeout 5.0 volume 2.5
    "Nana" "..........."
    "Nana" "..........."
    show nana bahagia at left
    play sound "typing.mp3" fadeout 5.0 volume 2.5
    play sound "suara nana 28.wav"
menu:
    "Nana" "Hai, kamu Ali ya, yang satu kelas sama aku?"
    "Iya":
        jump node3
    "Oh maaf siapa yaa":
        jump node4
        
label node4:
    scene hallway
    show nana malu_2 at left
    play sound "<from 1>suara nana 2.wav"
menu:
    "Nana" "Oh, maaf kalau aku salah orang..."
    "Oh Nana ya yang tadi, maaf saya lupa":
        jump node5


label node5:
    show nana bahagia at left
    play sound "suara nana 3.wav"
    "Nana" "Tidak apa-apa, senang bisa berkenalan denganmu!"
    jump node3

label node3:
    scene hallway
    show nana bahagia at left
    play sound "<from 1>suara nana 4.wav"
menu:
    "Nana" "Wah, kamu terlihat lebih tinggi yaa dari dekat"
    "Terima kasih, Nana":
        jump node6
    "Tidak, biasa saja":
        jump node7

label node7:
    scene hallway
    show nana malu_2 at left
    play sound "suara nana 5.wav"
    "Nana" "Tinggi tau dibanding aku"
menu:
    "hehe" :
        jump node6

label node6:
    scene hallway
    show nana bahagia at left
    play sound "<from 1>suara nana 6.wav"
menu:
    "Nana" "Btw, nanti jam 4 sore ayo main ke taman"
    "Boleh, kebetulan aku lagi tidak ada acara":
        jump node12
    "Maaf, aku tidak bisa ":
        jump node8
    
label node8:
    scene hallway
    show nana sedih at left
    play sound "suara nana 7.wav"
menu:
    "Nana" "Kenapaaa..?"
    "Aku hari ini mau les piano, lain kali aja yaa..":
        jump node9

label node9:
    scene hallway
    show nana malu_2 at left
    play sound "typing.mp3" fadeout 5.0 volume 2.5
menu:
    "Nana" "Janji yaa tapi..."
    "Iya janji ✌️":
        jump node10

label node10:
    scene hallway
    show nana malu_1 at left
    play sound "typing.mp3" fadeout 5.0 volume 2.5
    "Nana" "Yeeeeyyy"
    jump node32

label node32:
    scene blackscreen
    "Sementara itu...."
    with fade
    play music "nightm.mp3"
    scene summerfes
menu:
    "Hai mikoooo":
        jump node33
    "Malammm mikoo":
        jump node33

label node33:
    show miko terkejut at left
    play sound "<from 0.5>download (40).wav"
    "Miko" "Haloo, selamat malam juga Ali"
    show miko senang at left
    play sound "<from 0.6>download (41).wav"
menu:
    "Miko" "Kebetulan bgt ketemu ya hehe"
    "hehe(aslinya sih gamau diajak sama Nana)":
        jump node34
    "hehe(aslinya sih pengen ketemuan sama Miko)":
        jump node35

label node34:
    show miko terkejut at left
    play sound "<from 0.5>download (42).wav"
menu:
    "Miko" "eh kenapa kenapa nana?"
    "Eh enggak kok enggak kok":
        jump node36

label node35:
    show miko terkejut at left
    play sound "<from 0.5>download (42).wav"
menu:
    "Miko" "eh eh pengen apa tadi?"
    "Eh enggak enggak":
        jump node36

label node36:
    show miko senang at left
    play sound "<from 0.5>download (43).wav"
    "Miko" "Yaudah, Ayo kita jalan jalan bareng"
    hide miko senang
    pause 3
    "5 menit setelah merek jalan jalan..."
    show miko terkejut at left
    play sound "typing.mp3" fadeout 5.0 volume 2.5
menu:
    "Miko" "eh itu liat bagus ya komedi putar"
    "iya bagus banget":
        jump node37
    "kamu mau naik kah?":
        jump node38

label node37:
    show miko senang at left
    play sound "download (44).wav"
    "Miko" "Aku lebih tertarik sama komedi putarnya"
    show miko senang at left
    play sound "<from 0.4>download (45).wav"
menu:
    "Miko" "Kenapa ya saat kita naik komedi putar, kita merasa seperti terlempar keluar?"
    "Karena ada gaya sentrifugal dong":
        jump node39
    "Mungkin operatornya terlalu kencang":
        jump node40
    "Karena tiangnya mau putus":
        jump node40

label node38:
    show miko senang at left
    play sound "typing.mp3" fadeout 5.0 volume 2.5
    "Miko" "Eh engga kok"
    jump node37

label node39:
    play sound "<from 0.2>download (46).wav"
    "Miko" "Yak betul"
    play sound "download (47)(2).wav"
    "Miko" "Ketika kita berputar dengan cepat, tubuh kita ingin bergerak lurus karena inersia"
    show miko terkejut at left
    play sound "download (48)(2).wav"
    "Miko" "Tapi wahana memaksa kita berputar"
    show miko senang at left
    play sound "download (49)(2).wav"
menu: 
    "Miko" "Jadi kita merasa ada gaya yang mendorong kita ke luar"
    "Wah Miko kamu pintar sekali":
        jump node41
    "Detail sekali Miko mantap":
        jump node41

label node40:
    play sound "download (50).wav"
    "Miko" "Hey, Bukan gitu"
    play sound "<from 0.9>download (51).wav"
    "Miko" "Itu karena ada gaya sentrifugal"
    play sound "download (47)(2).wav"
    "Miko" "Ketika kita berputar dengan cepat, tubuh kita ingin bergerak lurus karena inersia"
    play sound "download (48)(2).wav"
    "Miko" "Tapi wahana memaksa kita berputar"
    play sound "download (49)(2).wav"
    "Miko" "Jadi kita merasa ada gaya yang mendorong kita ke luar"
menu:
    "Owh baru tau hehe":
        jump node42
    "Oalah gitu ternyata":
        jump node42

label node42:
    play sound "<from 0.5>download (52).wav"
    "Miko" "Eh Ali liat keatas"
    play sound "<from 0.4>download (53).wav"
    "Miko" "Bintang bintangnya cantik ya berkedip kedip trus"
    play sound "<from 0.4>download (54).wav"
    "Miko" "Kira kira kenapa yaa?"
menu:  
    "Karena yaa dari sananya":
        jump node43
    "Karena dilihat oleh orang cantik": 
        jump node43
    "Karena ada atmosfer bumi":
        jump node44


label node41:
    show miko marah at left
    play sound "typing.mp3" fadeout 5.0 volume 2.5
    "Miko" "Kamu juga yaa"
    show miko senang at left
    play sound "typing.mp3" fadeout 5.0 volume 2.5
    "Miko" "Eh Ali liat keatas"
    show miko terkejut at left
    play sound "typing.mp3" fadeout 5.0 volume 2.5
    "Miko" "Bintang bintangnya cantik ya berkedip kedip trus"
    show miko senang at left
    play sound "typing.mp3" fadeout 5.0 volume 2.5
menu:  
    "Miko" "Kira kira kenapa yaa?"
    "Karena yaa dari sananya":
        jump node43
    "Karena dilihat oleh orang cantik": 
        jump node43
    "Karena ada atmosfer bumi":
        jump node44


label node43:
    show miko marah at left
    play sound "<from 0.4>download (55).wav"
    "Miko" "Ih bukan lahh"
    show miko senang at left
    play sound "<from 0.4>download (56).wav"
    "Miko" "Itu karena atmosfer bumi. "
    play sound "<from 0.4>download (57)(2).wav"
    "Miko" "Saat cahaya bintang melewati atmosfer"
    play sound "<from 0.4>download (58)(2).wav"
menu:
    "Miko" "cahaya tersebut dibelokkan oleh lapisan udara yang bergerak menyebabkan bintang terlihat berkelap-kelip."
    "Hehe":
        jump node45
    "Wkwkwkw":
        jump node45

label node44:
    play sound "<from 0.6>download (59).wav"
    "Miko" "Betul sekali"
    play sound "<from 0.4>download (57)(2).wav"
    "Miko" "Saat cahaya bintang melewati atmosfer"
    play sound "<from 0.4>download (58)(2).wav"
    "Miko" "cahaya tersebut dibelokkan oleh lapisan udara yang bergerak"
    play sound "<from 0.4>download (60).wav"
menu:
    "Miko" "menyebabkan bintang terlihat berkelap-kelip."
    "Hebat Miko":
        jump node47
    "Selain cantik pintar juga yaa kamu Miko":
        jump node47

label node47:
    show miko malu at left
    play sound "<from 0.4>download (60).wav"
    "Miko""Eh ehhhhh"
    play sound "<from 0.6>download (61).wav"
    "Miko" "Kamu jugaaaa"
    show miko terkejut at left
    play sound "<from 0.6>download (62).wav"
menu:
    "Miko" "Loh kok sudah jam 10"
    "Iya juga ya, kalo mau pulang sekalian bareng aku saja":
        jump node48
    "Sini kuanterin nanti kecapean":
        jump node48
    
label node48:
    show miko malu at left
    play sound "<from 0.4>download (60).wav"
    "Miko" "Eh ehhhhh"
    show miko malu at left
    play sound "<from 0.4>download (63).wav"
    "Miko" "Gak ngerepotin kannn?"
    show miko senang at left
    play sound "<from 0.4>download (64).wav"
    "Miko" "Makasih banyak😍"
    jump ending4

label node45:
    show miko marah at left
    play sound "<from 0.4>download (65).wav"
    "Miko" "Alii... Kok kamu keliatan ngantuk sih"
    play sound "<from 0.6>download (66).wav"
menu:
    "Miko" "1+1 berapa"
    "1945":
        jump node46
    "3":
        jump node46

label node46:
    play sound "typing.mp3" fadeout 5.0 volume 2.5
    play sound "<from 0.5>download (67).wav"
    "Miko" "Itu tuh, kamu ngantuk itu"
    play sound "<from 0.5>download (68).wav"
    "Miko" "Aku juga mau pulang udh di cariin mama"
    play sound "<from 0.5>download (69).wav"
    "Miko" "Bye bye"
    jump ending3



label node12:
    scene hallway
    show nana bahagia at left
    play sound "suara nana 8.wav"
    "Nana" "Yeayy, baiklah sampai jumpa ditaman :)"
    jump node13

label node13:
    stop music
    play music "NO COPYRIGHT THEME PARK BACKGROUND MUSIC  CUTE BACKGROUND MUSIC.mp3"
    play sound "typing.mp3" volume 2.5
    scene taman
    "* tibalah jam 4 sore"
    show nana terkejut at left
    play sound "suara nana 10.wav"
    "Nana" "dududu, oh itu Ali. Ali aku ajak Miko nih biar ga sepi"
    jump node14

label node14:
    scene taman
    show miko senang at right
    show nana bahagia at left
    play sound "download (34).wav"
menu:
    "Miko" "Hai, ALi.."
    "Halooo":
        jump node15
    "Hai juga":
        jump node15

label node15:
    scene taman
    show miko senang at right
    show nana bahagia at left
    play sound "download (35).wav"
    menu:
        "Miko" "Kamu Ali murid baru di kelas yaa?"
        "Iya, Salam kenal Miko":
            jump node16
        
label node16:
    show miko senang at right
    play sound "<from 0.7>download (36).wav"
    "Miko" "Salam kenal juga Alii"

    show nana marah at left
    play sound "typing.mp3" volume 2.5
    "Nana" "..."
    jump node17

label node17:
    scene taman
    play sound "typing.mp3" volume 2.5
    "* Tidak terasa waktu demi waktu pun berlalu, jam sudah menunjukkan jam 5.15 sore"

    scene taman
    show miko senang at left
    play sound "<from 0.4>download (37).wav"
    menu:
        "Miko" "Sepertinya sudah terlalu sore. Aku pulang duluan ya..."
        "Mau kuanterin pulang ga?":
            jump node18
        "(pura-pura habis bensin)":
            jump node19

label node18:
    hide miko senang
    show nana marah at left
    play sound "typing.mp3" volume 2.5
    "Nana" "....."
    hide nana marah
    show miko senang at left
    play sound "download (38).wav"
    "Miko" "Oh gak usah, aku naik Taxi aja. Makasih tawarannya Ali"
    jump node19

label node19:
    scene taman
    hide miko terkejut
    show nana bahagia at left
    play sound "typing.mp3" volume 2.5
    play sound "suara nana 29.wav"
    menu:
        "Nana" "Hati hati Miko.."
        "Hati hati Miko":
            jump node20
label node20:
    hide nana bahagia
    show miko senang at right
    play sound "download (39).wav"
    "Miko" "Makasih teman teman"
    hide miko senang
    show nana malu_1
    play sound "suara nana 11.wav"
    "Nana" "Ayo ali kita pulang juga. btw kamu mau mampir makan malam dirumahku ga?"
    play sound "suara nana 30.wav"
menu:
    "Nana" "setelah itu baru kamu pulang"
    "Boleh juga":
        jump node22
    "Maaf aku tidak bisa, nanti mamah marah :)":
        jump node21

label node21:
    scene taman
    show nana sedih at center
    play sound "suara nana 12.wav"
menu:
    "Nana" "Yakin? dirumahku lagi ga ada siapa siapa juga, dan aku juga penakut orangnya 🥺"
    "GASSS, HAYYUKKK":
        jump node22

    "Maaf tetap tidak bisa":
        jump ending1

label node22:
    show nana bahagia at center
    play sound "suara nana 13.wav"
    "Nana" "Yeayyy, ayo berangkaat.."

    scene taman
    play sound "typing.mp3" volume 2.5
    "* Merekapun berjalan bersama sama hingga kerumah Nana"
    jump node23

label node23:
    with fade
    scene dalam rumah2
    play music "1 Minute Timer Lofi.mp3"
    show nana bahagia at left
    play sound "<from 0.8>suara nana 14.wav"
    "Nana" "Akhirnya sampai juga, ga sabar mau makan berdua :)"
    play sound "suara nana 15.wav"
menu:
    "Nana" "Kita makan mie cup saja ya, sebentar aku masakin ya..."
    "Iya":
        jump node24
label node24:
    hide nana bahagia
    pause 3
    "5 menit kemudian..."
    with fade
    show nana bahagia at left
    play sound "suara nana 16.wav"
    "Nana" "Sudah selesai..."
    play sound "<from 0.3>suara nana 17.wav"
    menu:
        "Nana" "ittadakimassu , selamat makan"
        "Bismillah":
            jump node25
            
label node25:
    pause 3
    scene dalam rumah2
    show nana malu_2 at left
    play sound "<from 0.3>suara nana 18.wav"
    "Nana" "yeay kenyang. Maaf yah cuman makan mie cup"
    show nana malu_1
    play sound "suara nana 31.wav"
    menu:
        "Nana" "Tapi jangan dilihat dari makanan yang di makan tapi lihat makan bareng siapa 😌"
        "Hmmmm":
            jump node26
label node26:
    stop music
    play music "Ngobrol.mp3"
    stop audio
    scene dalam rumah2
menu:
    "Udah mulai larut nih...":
        jump node28

label node28:
    show nana sedih at left
    "Nana" "......"
    show nana malu_2
    play sound "<from 0.3>suara nana 19.wav"
menu:
    "Nana" "Ali.., Sebelum kamu pulang aku mau nanya boleh ya?!"
    "Hmmm...boleh":
        jump node29
    "Maaf udah larut banget sih, nanti dimarahin mamah":
        jump ending1

label node29:
    play sound "<from 0.3>suara nana 20.wav"
menu:
    "Nana" "Kan tadi ada si Miko, menurutmu apakah dia lebih cantik daripada aku?"
    "Gk kok, menurutku kamu lebih cantik daripada Miko ":
        jump node30

    "yaa lumayann..., kenapa emangnya?":
        jump ending1

label node30:
    scene dalam rumah2
    show nana malu_2 at left
    play sound "<from 0.7>suara nana 21.wav"
    "Nana" "Ehh eh kamuu...."
    show nana malu_1 at left
    play sound "<from 0.4>suara nana 22.wav"
    "Nana" "Maksudkuu, Terima kasih..."
    show nana terkejut at left
    play sound "suara nana 23.wav"
    "Nana" "Sepertinya sudah terlalu malam, sebaiknya kamu pulang"
    show nana malu_1 at left
    play sound "suara nana 24.wav"
menu:
    "Nana" "Sebelum kamu pulang, titip setengah hatiku ini buatmu"
    "oh yaa, setengah hatiku juga akan ku tinggal disini, jaga baik baik yaa":
        jump node31

label node31:
    show nana malu_2 at left
    play sound "<from 0.6>suara nana 25.wav"
    "Nana" "Eh eh eh"
    show nana bahagia at left
    play sound "suara nana 26.wav"
    "Nana" "Akan ku jaga sangat sangat baik, punyaku juga yaaa"
    jump ending2


label ending1:
    stop sound
    "pulang kerumah"
    jump endingComm

label ending2:
    scene dalam rumah2
    show nana bahagia at left
    play sound "suara nana 27.wav"
    "Nana" "Baiklah, hati hati dijalan sampai jumpa besok"
    jump endingSuccNana

label ending3:
    "gagal jadian dengan miko"
    jump endingFailMiko

label ending4:
    "berhasil jadian dengan miko"
    jump endingSuccMiko



label endingComm:
    stop music
    play sound "GTA San Andreas - Mission passed sound.mp3"
    scene ending common with fade
    pause 10
    return
label endingSuccNana:
    stop music
    play sound "endd2.mp3"
    scene ending rel nana with fade
    pause 10
    return
label endingFailMiko:
    stop music
    play sound "endd3.mp3"
    scene ending fail miko with fade
    pause 10
    return
label endingSuccMiko:
    stop music
    play sound "endd4.mp3"
    scene ending suc miko with fade
    pause 10
    return