package spacy

class ProcessController {

    def index() {
        String snert = new File("/model/snert.py").getText('UTF-8')
        String g = snert.replace("--text--", params.txt.toString().replace("\n", ""))
        File nerpy = new File("/model/sner.py")
        nerpy.text = g

        String cmd = 'python /model/sner.py'

        def sout = new StringBuilder(), serr = new StringBuilder()
        def proc = cmd.execute()
        proc.consumeProcessOutput(sout, serr)
        proc.waitFor()
//        println "out> $sout err> $serr"

        def ners = sout.toString().split("\n")

        ArrayList<HashMap<String, String>> spacy = new ArrayList<>()

        if (ners.size() > 0) {
            ners.each { line ->
                def data = line.split("---")
                spacy.add([name: data[0], value: data[1]])
            }
        }
        println(sford(params.txt))

        render view: "index", model: [txt: params.txt, spacy: spacy, sford: null]
    }

    private static def sford(String text) {
        String dirLoc = "/model"

        File pred = new File("${dirLoc}/pred.txt")
        pred.text = text

        String scriptdir = "/Users/styl3r/PycharmProjects/spa/model"
        def sout = new StringBuilder(), serr = new StringBuilder()
        def ner = "java -mx3g -cp \"$scriptdir/stanford-ner.jar:$scriptdir/lib/*\" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier $scriptdir/classifiers/ner-model.ser.gz -textFile $scriptdir/pred.txt -outputFormat inlineXML".execute()
//        ner.consumeProcessOutput(sout, serr)

//        println "out> $sout err> $serr"


        ner.waitFor()

        String nerResult = ner.text
        println(nerResult)

        nerResult += "\n"

        def location = '''/bin/bash -c "java -mx3g -cp \\\"$scriptdir/stanford-ner.jar:$scriptdir/lib/*\\\" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier $scriptdir/classifiers/ner-model.ser.gz -textFile $scriptdir/pred.txt -outputFormat inlineXML"'''
        println(location)
        location = location.execute()
        location.consumeProcessOutput(sout, serr)
        location.waitFor()
        println "out> $sout err> $serr"
        nerResult += sout

        nerResult += location.text

        String template = new File("/model/ner_template.py").getText('UTF-8')

        String g = template.replace("--text--", nerResult)
        File nerpy = new File("/model/ner.py")
        nerpy.text = g

        def reg = "python /model/ner.py".execute()
        String result = reg.text

        result
    }
}
