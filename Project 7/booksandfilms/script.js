// ნიმუშ მონაცემები (ფილმები და წიგნები)
const sampleData = [
    { id: 1, type: 'movie', title: 'ავატარი', year: 2009, genre: 'ფანტასტიკა', rating: 4.5, director: 'ჯეიმს კამერონი', description: 'ადამიანები უცხო პლანეტაზე და მათი ბრძოლა ბუნებასთან.' },
    { id: 2, type: 'book', title: 'ვეფხისტყაოსანი', year: 1200, genre: 'პოემა', rating: 5.0, author: 'შოთა რუსთაველი', description: 'ქართული ეროვნული პოემა, რომელიც სიყვარულსა და ვაჟკაცობაზე მოგვითხრობს.' },
    
    // ფილმები
    { id: 3, type: 'movie', title: 'ინტერსტელარი', year: 2014, genre: 'ფანტასტიკა', rating: 4.9, director: 'კრისტოფერ ნოლანი', description: 'კოსმოსური მოგზაურობა კაცობრიობის გადასარჩენად.' },
    { id: 4, type: 'movie', title: 'ინსეპშენი', year: 2010, genre: 'თრილერი', rating: 4.8, director: 'კრისტოფერ ნოლანი', description: 'სიზმრების სამყაროში ჯაშუშური მისია.' },
    { id: 5, type: 'movie', title: 'ბეტმენი: ბნელი რაინდი', year: 2008, genre: 'ექშენი', rating: 5.0, director: 'კრისტოფერ ნოლანი', description: 'ბეტმენის ბრძოლა ჯოკერთან.' },
    { id: 6, type: 'movie', title: 'გლადიატორი', year: 2000, genre: 'ისტორიული დრამა', rating: 4.7, director: 'რიდლი სკოტი', description: 'რომის იმპერიის დროინდელი მეომრის ისტორია.' },
    { id: 7, type: 'movie', title: 'შინდლერის სია', year: 1993, genre: 'დრამა', rating: 5.0, director: 'სტივენ სპილბერგი', description: 'ნამდვილი ისტორია ჰოლოკოსტზე.' },
    { id: 8, type: 'movie', title: 'ტიტანიკი', year: 1997, genre: 'მელოდრამა', rating: 4.8, director: 'ჯეიმს კამერონი', description: 'ტრაგიკული სიყვარულის ისტორია გემზე.' },
    { id: 9, type: 'movie', title: 'მატრიცა', year: 1999, genre: 'ფანტასტიკა', rating: 4.9, director: 'ლანა და ლილი ვაჩოვსკები', description: 'ვირტუალური რეალობის საიდუმლოებები.' },
    { id: 10, type: 'movie', title: 'ფორესტ გამპი', year: 1994, genre: 'დრამა', rating: 4.9, director: 'რობერტ ზემეკისი', description: 'ადამიანის საოცარი ისტორია, რომელიც უნიკალური ხედვით უყურებს ცხოვრებას.' },
    
    // წიგნები
    { id: 11, type: 'book', title: '1984', year: 1949, genre: 'ანტიუტოპია', rating: 4.9, author: 'ჯორჯ ორუელი', description: 'მთელი ცხოვრების კონტროლი ტოტალიტარული რეჟიმის მიერ.' },
    { id: 12, type: 'book', title: 'ციცინათელა', year: 1933, genre: 'რომანი', rating: 4.8, author: 'გრიგოლ რობაქიძე', description: 'ქართული კლასიკური რომანი.' },
    { id: 13, type: 'book', title: 'მარტოობის ასი წელი', year: 1967, genre: 'მაგიური რეალიზმი', rating: 4.9, author: 'გაბრიელ გარსია მარკესი', description: 'ბუენდიათა ოჯახის საგა.' },
    { id: 14, type: 'book', title: 'ოსტატი და მარგარიტა', year: 1966, genre: 'ფანტასტიკა', rating: 4.9, author: 'მიხაილ ბულგაკოვი', description: 'სატირა, ფილოსოფია და ფანტასტიკა ერთიანად.' },
    { id: 15, type: 'book', title: 'ჰობიტი', year: 1937, genre: 'ფენტეზი', rating: 4.8, author: 'ჯ.რ.რ. ტოლკინი', description: 'ბილბო ბეგინსის თავგადასავალი.' },
    { id: 16, type: 'book', title: 'პატარა პრინცი', year: 1943, genre: 'ალეგორიული ზღაპარი', rating: 5.0, author: 'ანტუან დე სენტ-ეგზიუპერი', description: 'ბავშვის თვალით დანახული სიბრძნე.' },
    { id: 17, type: 'book', title: 'ომი და მშვიდობა', year: 1869, genre: 'ისტორიული რომანი', rating: 4.7, author: 'ლევ ტოლსტოი', description: 'რუსეთის არისტოკრატიის და ომის ისტორია.' }
];


// მიმდინარე ფილტრი ("all" ნიშნავს რომ ყველა ნაჩვენებია)
let currentFilter = 'all';
// მონაცემების მასივი, რომელიც ამჟამად ნაჩვენებია
let currentData = sampleData;

// გვერდის ჩვენების ფუნქცია
function showPage(pageId) {
    // ყველა ".page" ელემენტს მოვხსნით active კლასს
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    // არჩეულ გვერდს დავამატებთ active კლასს
    document.getElementById(pageId).classList.add('active');
    // თუ მთავარი გვერდია, მაშინ ნაჩვენები იქნება ყველა მონაცემი
    if (pageId === 'home') displayResults(currentData, 'homeResults');
}

// ფილტრის დაყენება (ფილმები/წიგნები/ყველა)
function setFilter(type) {
    currentFilter = type; // შევინახავთ არჩეულ ფილტრს
    // ყველა ფილტრის ღილაკს მოვხსნით active კლასს
    document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
    // არჩეულ ღილაკს დავუმატებთ active-ს
    event.target.classList.add('active');
    // თუ "all" არჩეულია, ვაჩვენებთ ყველა მონაცემს,
    // წინააღმდეგ შემთხვევაში ვფილტრავთ (movie/book)
    const filtered = type === 'all' ? sampleData : sampleData.filter(i => i.type === type.slice(0, -1));
    // ნაჩვენებია გაფილტრული შედეგები
    displayResults(filtered, 'homeResults');
}

// ძიების ფუნქცია
function performSearch() {
    // ვიღებთ ტექსტს მთავარ ან საძიებო გვერდის input-დან
    const query = document.getElementById('mainSearch').value || document.getElementById('searchPageInput').value;
    // თუ ცარიელია, გაფრთხილება
    if (!query.trim()) { alert('გთხოვთ შეიყვანოთ ტექსტი'); return; }
    // ვფილტრავთ sampleData-ს (სათაურის, ჟანრის, რეჟისორის ან ავტორის მიხედვით)
    const results = sampleData.filter(item =>
        item.title.toLowerCase().includes(query.toLowerCase()) ||
        item.genre.toLowerCase().includes(query.toLowerCase()) ||
        (item.director && item.director.toLowerCase().includes(query.toLowerCase())) ||
        (item.author && item.author.toLowerCase().includes(query.toLowerCase()))
    );
    // ვაჩვენებთ შედეგებს
    displayResults(results, 'searchResults');
    // input-ში ვტოვებთ შეყვანილ ტექსტს
    document.getElementById('searchPageInput').value = query;
    // გადავდივართ ძიების გვერდზე
    showPage('search');
}

// შედეგების ჩვენების ფუნქცია
function displayResults(data, containerId) {
    const container = document.getElementById(containerId);
    // თუ შედეგი არ არის, ვწერთ ტექსტს
    if (data.length === 0) { container.innerHTML = '<p>შედეგები არ მოიძებნა</p>'; return; }
    // ვფილტრავთ მონაცემებს currentFilter-ის მიხედვით
    const filteredData = currentFilter === 'all' ? data : data.filter(i => currentFilter === 'movies' ? i.type === 'movie' : i.type === 'book');
    // თითოეული ელემენტისთვის ვქმნით HTML ბლოკს (ქარდი)
    container.innerHTML = filteredData.map(item => `
        <div class="item-card" onclick="showDetails(${item.id})">
            <div class="item-image">${item.type === 'movie' ? '🎬' : '📚'}</div>
            <div class="item-info">
                <div class="item-title">${item.title}</div>
                <div class="item-meta">${item.year} • ${item.genre}<br>${item.type === 'movie' ? 'რეჟისორი: '+item.director : 'ავტორი: '+item.author}</div>
                <div class="rating">${'★'.repeat(Math.floor(item.rating))} ${item.rating}/5</div>
            </div>
        </div>
    `).join('');
}

// დეტალების გვერდის ჩვენება
function showDetails(id) {
    // sampleData-ში ვპოულობთ ელემენტს ID-ის მიხედვით
    const item = sampleData.find(i => i.id === id);
    const detailContent = document.getElementById('detailContent');
    // ვქმნით დეტალური ინფორმაციის HTML-ს
    detailContent.innerHTML = `
        <div class="detail-image">${item.type === 'movie' ? '🎬' : '📚'}</div>
        <div class="detail-info">
            <h1>${item.title}</h1>
            <div class="detail-meta">
                <div><strong>წელი:</strong> ${item.year}</div>
                <div><strong>ჟანრი:</strong> ${item.genre}</div>
                <div><strong>${item.type === 'movie' ? 'რეჟისორი' : 'ავტორი'}:</strong> ${item.type === 'movie' ? item.director : item.author}</div>
                <div class="rating"><strong>შეფასება:</strong> ${'★'.repeat(Math.floor(item.rating))} ${item.rating}/5</div>
            </div>
            <div class="detail-description"><h3>აღწერა:</h3><p>${item.description}</p></div>
            <button class="btn" onclick="showPage('home')">მთავარ გვერდზე დაბრუნება</button>
        </div>
    `;
    // გადავდივართ დეტალების გვერდზე
    showPage('details');
}

// ინიციალიზაცია (როცა გვერდი ჩაიტვირთება)
document.addEventListener('DOMContentLoaded', () => {
    // საწყისად ვაჩვენებთ sampleData-ს მთავარ გვერდზე
    displayResults(sampleData, 'homeResults');
    // მთავარ საძიებო ველში Enter-ზე დაჭერისას ვიწყებთ ძიებას
    document.getElementById('mainSearch').addEventListener('keypress', e => { if (e.key === 'Enter') performSearch(); });
    // ძიების გვერდის input-შიც იგივე
    document.getElementById('searchPageInput').addEventListener('keypress', e => { if (e.key === 'Enter') performSearch(); });
});
