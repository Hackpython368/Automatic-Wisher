function renderCards() {
      cardContainer.innerHTML = "";
      cardData.forEach((data, index) => {
        const card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `
          <h3>${data[0]}</h3>
          <div class="date">${data[2]}</div>
          <p>${data[4]}</p>
        `;
        card.onclick = () => openModal(index);
        cardContainer.appendChild(card);
      });
    }