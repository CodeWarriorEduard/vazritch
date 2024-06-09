import { useEffect, useState } from "react";
import Header from "../../components/Header/Header";
import EditorC from "../../components/Editor/EditorC";
import Footer from "../../components/Footer/Footer";
import { BarLoader } from "react-spinners";

function Home(){
    const [loading, setLoading] = useState(false);

    

    useEffect(() => {
      setLoading(true);
      setTimeout(()=>{
        setLoading(false);
      },1300);
    }, [])
    

   


    return (
      <div className = "principal" style={{height:"100vh"}}>
        {
          loading ?(
              <div className='loading-container'>
                <h2>VAZRITCH</h2>
                <BarLoader color={'#FFFFFF'} aria-label='VAZRITCH' loading={loading}/>
              </div>
          ):(
            <>
              <Header/>
              <EditorC/>
              <Footer/>
            </>
          )
        }
      </div>
    )

}


export default Home;