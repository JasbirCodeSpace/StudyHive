function makeThumb(page) {
    // draw page to fit into 96x96 canvas
    var vp = page.getViewport({scale:1});
    var canvas = document.createElement("canvas");
    const scaleSize = 0.5;
    // canvas.width = vp.width * scaleSize;
    // canvas.height = vp.height * scaleSize;
    canvas.width = 250;
    canvas.height = 360;

    var scale = Math.min(canvas.width / vp.width, canvas.height / vp.height);

    return page.render({ canvasContext: canvas.getContext("2d"), viewport: page.getViewport({ scale: scale }) }).promise.then(function () {
      return canvas;
  });
}


const updateCanvas = async(url, popular=false, count=4)=>{

  const response = await fetch(url, {
      method: 'POST',
      body:JSON.stringify({
        popular: popular,
        count: count,
      }),
  });
  const filePaths = await response.json();
  filePaths.forEach(file => {
    const {path, pk} = file;
     pdfjsLib.getDocument(path).promise.then(async function (doc) {
         const canvas = await doc.getPage(1).then(makeThumb)
         canvas.style.width = "100%";
         canvas.style.height = "auto";
        const thumbDiv = document.getElementById(`file-${pk}`);
        thumbDiv.appendChild(canvas);
      }).catch(console.error);
  });
};