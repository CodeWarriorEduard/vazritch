import MenuIcon from '@mui/icons-material/Menu';
import './Header.styles.css'
import { IconButton } from '@mui/material';
import Options from '../Options/Options';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import vazritch from '../../assets/vazritch.png'

function Header() {
   
  const [open, setOpen] = useState(false);

  const handleMenuOpen = () =>{
    setOpen(!open);
  }

  return (
    <header>
          <Link to={"/"}><img src={vazritch} alt="vazritch-logo" style={{width:"300px", height:"220px"}}/></Link>
          <Options isOpen={open}/>
          <IconButton onClick={handleMenuOpen} className='container-btn'>
            <MenuIcon className='menu-btn'/>
          </IconButton>
    </header>
  )
}

export default Header