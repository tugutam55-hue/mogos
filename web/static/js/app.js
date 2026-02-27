function parseKey(text){

  const lines = text.split("\n")

  const obj = {}

  for(let line of lines){

    line=line.trim()
    if(!line) continue

    const [q,a]=line.split(":")
    obj[q.trim()] = a.trim()
  }

  return obj
}


async function saveKey(){

  const text = document.getElementById("key").value

  const data = parseKey(text)

  await fetch("/api/set-key",{
    method:"POST",
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify(data)
  })

  alert("Kunci tersimpan")
}


async function saveTemplate(){

  const text = document.getElementById("template").value

  const data = JSON.parse(text)

  await fetch("/api/set-template",{
    method:"POST",
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify(data)
  })

  alert("Template tersimpan")
}


async function scan(){

  const fileInput = document.getElementById("file")

  const form = new FormData()

  form.append("file", fileInput.files[0])

  const res = await fetch("/api/scan",{
    method:"POST",
    body:form
  })

  const data = await res.json()

  document.getElementById("result").textContent =
      JSON.stringify(data,null,2)
    }
