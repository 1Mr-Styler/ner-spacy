<!doctype html>
<html>
<head>
    <meta name="layout" content="main"/>
    <title></title>
</head>

<body>
<div class="grid-container">
    <div class="SpaCy">
        <ul class="list-group">
            <g:each in="${spacy}" var="sp">
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    ${sp.value}
                    <span class="badge badge-primary badge-pill">${sp.name}</span>
                </li>
            </g:each>
        </ul>
    </div>

    <div class="Stanford">
        <ul class="list-group">
            <g:each in="${sford}" var="sf">
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    ${sf.value}
                    <span class="badge badge-primary badge-pill">${sf.name}</span>
                </li>
            </g:each>
        </ul>
    </div>

    <div class="Input">
        <form method="post">
            <textarea style="width: 90%; height: 90%" rows="10" name="txt">${txt}</textarea>
            <button type="submit">NER</button>
        </form>
    </div>
</div>

</body>
</html>


<ul class="list-group">

    <li class="list-group-item d-flex justify-content-between align-items-center">
        Dapibus ac facilisis in
        <span class="badge badge-primary badge-pill">2</span>
    </li>
    <li class="list-group-item d-flex justify-content-between align-items-center">
        Morbi leo risus
        <span class="badge badge-primary badge-pill">1</span>
    </li>
</ul>