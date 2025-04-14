const API = "http://127.0.0.1:8001";

document.addEventListener("DOMContentLoaded", () => {
  cargarCandidatos();
  cargarOfertas();
  cargarOrdenes();


  document.getElementById("form-candidato").addEventListener("submit", async (e) => {
    e.preventDefault();
    const form = e.target;
    const data = {
      nombre: form.nombre.value,
      apellido: form.apellido.value,
      tipo_documento: form.tipo_documento.value,
      cedula: form.cedula.value,
      fecha_nacimiento: form.fecha_nacimiento.value || null,
      rh: form.rh.value,
      ciudad_expedicion: form.ciudad_expedicion.value,
      ciudad_nacimiento: form.ciudad_nacimiento.value,
      ciudad_domicilio: form.ciudad_domicilio.value
    };

    try {
      const res = await fetch(`${API}/candidatos/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      if (!res.ok) {
        const error = await res.json();
        throw new Error(error.detail || "Error al registrar candidato");
      }

      alert("✅ Candidato creado exitosamente");
      form.reset();
      cargarCandidatos();
    } catch (err) {
      alert("❌ " + err.message);
      console.error(err);
    }
  });


  document.getElementById("form-oferta").addEventListener("submit", async (e) => {
    e.preventDefault();
    const form = e.target;
    const data = {
      cliente: form.cliente.value,
      cargo: form.cargo.value,
      descripcion: form.descripcion.value,
      ciudad: form.ciudad.value
    };

    try {
      const res = await fetch(`${API}/ofertas/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      if (!res.ok) throw new Error("Error al registrar oferta");
      alert("✅ Oferta registrada");
      form.reset();
      cargarOfertas();
    } catch (err) {
      alert("❌ " + err.message);
    }
  });

  
  document.getElementById("form-orden").addEventListener("submit", async (e) => {
    e.preventDefault();
    const form = e.target;
    const data = {
      cliente: form.cliente.value,
      cargo: form.cargo.value,
      examenes: form.examenes.value
    };

    try {
      const res = await fetch(`${API}/ordenes/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
      });

      if (!res.ok) throw new Error("Error al registrar orden");
      alert("✅ Orden registrada");
      form.reset();
      cargarOrdenes();
    } catch (err) {
      alert("❌ " + err.message);
    }
  });
});



async function cargarCandidatos() {
  const tbody = document.querySelector("#tabla-candidatos tbody");
  tbody.innerHTML = "";

  try {
    const res = await fetch(`${API}/candidatos/`);
    const candidatos = await res.json();

    candidatos.forEach((c, index) => {
      const fila = document.createElement("tr");
      fila.innerHTML = `
        <td>${index + 1}</td>
        <td>${c.nombre}</td>
        <td>${c.apellido}</td>
        <td>${c.cedula}</td>
        <td>${c.rh}</td>
        <td>${c.ciudad_domicilio}</td>
      `;
      tbody.appendChild(fila);
    });
  } catch (err) {
    const fila = document.createElement("tr");
    fila.innerHTML = `<td colspan="6" class="text-danger text-center">Error al cargar candidatos</td>`;
    tbody.appendChild(fila);
  }
}

async function cargarOfertas() {
  const tbody = document.querySelector("#tabla-ofertas tbody");
  tbody.innerHTML = "";

  try {
    const res = await fetch(`${API}/ofertas/`);
    const ofertas = await res.json();

    ofertas.forEach((o, index) => {
      const fila = document.createElement("tr");
      fila.innerHTML = `
        <td>${index + 1}</td>
        <td>${o.cliente}</td>
        <td>${o.cargo}</td>
        <td>${o.ciudad}</td>
      `;
      tbody.appendChild(fila);
    });
  } catch (err) {
    const fila = document.createElement("tr");
    fila.innerHTML = `<td colspan="4" class="text-danger text-center">Error al cargar ofertas</td>`;
    tbody.appendChild(fila);
  }
}

async function cargarOrdenes() {
  const tbody = document.querySelector("#tabla-ordenes tbody");
  tbody.innerHTML = "";

  try {
    const res = await fetch(`${API}/ordenes/`);
    const ordenes = await res.json();

    ordenes.forEach((o, index) => {
      const fila = document.createElement("tr");
      fila.innerHTML = `
        <td>${index + 1}</td>
        <td>${o.cliente}</td>
        <td>${o.cargo}</td>
        <td>${o.examenes}</td>
      `;
      tbody.appendChild(fila);
    });
  } catch (err) {
    const fila = document.createElement("tr");
    fila.innerHTML = `<td colspan="4" class="text-danger text-center">Error al cargar órdenes</td>`;
    tbody.appendChild(fila);
  }
}
