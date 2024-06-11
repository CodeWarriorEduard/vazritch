import axios from "axios"
import Header from "../../components/Header/Header";
import { useEffect, useState } from "react"
import Showdown from "showdown";
import '../Styles/Docs.styles.css'
import { BarLoader } from "react-spinners";
import Footer from "../../components/Footer/Footer";


function Docs() {
  const converter = new Showdown.Converter();
  const [data, setData] = useState<string | undefined>(undefined);
  const [loading, setLoading] = useState(false);

  const infoHl = [
    "Arquitectura",
    "Tipos de datos",
    "Declaración de variables",
    "Comentarios",
    "Imprimir en pantalla",
    "Operaciones matemáticas básicas",
    "Condicionales"
  ];
 
  const url = "https://raw.githubusercontent.com/CodeWarriorEduard/vazritch/main/README.md"

  const fetchMd = () =>{
    axios.get(url)
    .then((response)=>{
      const htmlT = converter.makeHtml(response.data);
      setData(htmlT);
    })
    .catch(error =>{
      console.error(error)
    })
  }

  useEffect(() => { 
    fetchMd()
  }, [data]);

  useEffect(() => {
    setLoading(true);
    setTimeout(()=>{
      setLoading(false);
    },1300);
  }, [])


  const findWord = (e:string) => {  
    const elements = document.querySelectorAll('.info-data h2, .info-data h3');
    elements.forEach(element => {
      const text = element.innerHTML;
      if (text.includes(e)) {
        const offset = element.getBoundingClientRect();

        window.scrollTo(offset.left + window.scrollX, offset.top-80 + window.scrollY);
      }
    });
  };


  return (
    <div>
      {
        loading? (

          <div className='loading-container' style={{height:"100vh"}}>
          <h2>VAZRITCH</h2>
          <BarLoader  color={'#FFFFFF'} aria-label='VAZRITCH' loading={loading}/>
          </div>
  
        ):(
          <div style={{backgroundColor:"#434242", paddingBottom: "20px"}}>
          <Header/>
          <div className=" info-content-container">
            
            <div className=" info-sidebar">
                <ul className="info-sidebar-content">
                {infoHl.map((el, index) => (
                   <li key={index} onClick={()=> findWord(el)}>{el}</li>
                    ))}
                </ul>
            </div>

          <div dangerouslySetInnerHTML={{__html: data || ''}} style={{color:"black"}} className="info-data wrapper"></div>

          </div>
          <Footer/>
        </div>
        )
      }

    </div>
  )
}

export default Docs