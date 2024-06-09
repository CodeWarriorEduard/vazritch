import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Home from '../pages/Home/Home';
import Docs from '../pages/Docs/Docs';


function RouterProv(){
    
    const routes = createBrowserRouter([
        {path:"/",
        Component:Home,
        },
        {path:"/info",
        Component:Docs
        },
    ]);
    
    return(
       <RouterProvider router={routes}></RouterProvider>
    )
}


export default RouterProv