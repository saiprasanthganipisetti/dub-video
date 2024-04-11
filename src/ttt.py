""" ttt.py
    INPUT  : English srt file(english_srt.srt) generated from srt.py
    OUTPUT : Target language srt file(translates_srt.srt) and an array(srt_array) in the form [[1,'00.0','04.0',"Welcome, everyone."]]
    It accepts an srt file in English language.
    Then translates each subtitle into target language.
    Meanwhile it also generates an srt file called translated_srt.srt containg TARGET LANGUAGE subtitles.
"""

import mtranslate as mt

class Translate:
    def proper_srt(self,url):
        file = open(url,'r',encoding='utf-8')
        f = file.read()
        l = f.split('\n')
        t = []
        fin = []
        count = 1
        for i in l:
            i = i.strip()
            if i == '':
                t.insert(0,count)
                fin.append(t)
                t = []
                count += 1
            elif '-->' in i:
                p = i.split('-->')
                t.append(p[0].strip())
                t.append(p[1].strip())
            else:
                if len(t) == 2:
                    t.append(i)
                elif len(t) == 3:
                    t[2] += ' '+i
        return fin


    def translate_text(self,srt_file, lang):
        srt_array = self.proper_srt(srt_file)[:-1]
        # print(srt_array)
        d = {"Hindi": "hi","Bengali": "bn","Telugu": "te","Tamil": "ta","Marathi": "mr","Urdu": "ur","Gujarati": "gu","Kannada": "kn","Odia": "or","Malayalam": "ml","Punjabi": "pa","Assamese": "as","Maithili": "mai","Santali": "sat","Kashmiri": "ks","Nepali": "ne","Konkani": "kok","Sindhi": "sd","Manipuri": "mni","Dogri": "dgo","Bodo": "brx","Sanskrit": "sa"}
        filename = "subtitles/"+lang+"_srt.srt"
        wr = open(filename,'w',encoding='utf-8')
        for i in range(len(srt_array)): #srt is an array in the form:[[1,'00.0','04.0',"Welcome, everyone."]]
            count, start_time, end_time, text = srt_array[i]
            translated_text = mt.translate(text, d[lang])
            srt_array[i][3] = translated_text
            wr.write(f"{count}\n{start_time} --> {end_time}\n{translated_text}\n\n") #It is the step that makes translated_srt.srt
        return srt_array

