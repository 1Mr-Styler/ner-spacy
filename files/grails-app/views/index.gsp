<!doctype html>
<html>
<head>
    <meta name="layout" content="main"/>
    <title></title>
</head>

<body>
<div class="grid-container">
    <div class="SpaCy">
        <g:each in="${spacy}" var="sp">
            <div class="form-group">

                <label for="${sp.name}">
                    ${sp.name}
                </label>
                <input type="text" value="${sp.value}" class="form-control" id="${sp.name}"/>
            </div>
        </g:each>
    </div>

    <div class="Stanford">
        <g:each in="${sford}" var="sf">
            <div class="form-group">

                <label for="${sford.name}">
                    ${sford.name}
                </label>
                <input type="text" value="${sford.value}" class="form-control" id="${sford.name}"/>
            </div>
        </g:each>
    </div>

    <div class="Input">
        <form method="post" action="${createLink(controller: "process")}">
            <textarea style="width: 90%; height: 90%" rows="10" name="txt"></textarea>
            <button type="submit">NER</button>
        </form>
    </div>
</div>

</body>
</html>
