function fun_ubicacionnio( $atts = array() ) {    
	$provincia = $_GET["prov"];  
    extract( shortcode_atts( array( 'texto' => '00'  ), $atts ) );	
	$location = "<span class='apolo-geo-city'></span>";
	$mensaje = "<div class='apolo-geo-show' style='display: none;'>Tenemos <span class='apolo-geo-number' data-min='10' data-max='40'></span> visitantes buscando bodegas para encontrar un buen vino.</div>";
    $plantilla = "<H2>Buscando Bodegas cerca de: $location</H2><p>Encuentra la mejor bodega desde: <strong> >>>$location<<< </strong></p><div class='apolo-geo-hide'>Buscando vino cerca...</div>";
    $texto = $plantilla;
	$titulo = "<quote>$mensaje</quote><br><H2>Hemos encontrado las siguientes bodegas en: <u>$provincia</u>:</H2><p>bla bla bla</p><p>bla bla bla</p>";
    return $titulo.$texto;
}
add_shortcode('SC_UBICACION','fun_ubicacionnio');

// mostramos listado de provincias
function post_fun_provincias($atts){
//consulta BBDD --- 
	$link = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);	
    $sql = "SELECT * FROM z_provincias ORDER BY nombre asc";
	if($result = mysqli_query($link, $sql)){
		if(mysqli_num_rows($result) > 0){
			while($row = mysqli_fetch_array($result)){    
				$nombre = $row['nombre'];
				$nombre = str_replace("%27","",$nombre);
				$emoji = "🍷";
				$cadena = $cadena."<button type=\"button\" class=\"list-primary bod_list\"><a class='linkcom' alt='bodega en ".$nombre."' href=la-mejores-bodegas-de-espana?prov=".$nombre.">".$nombre."</a> <span class=\"list-light comemoji\">".$emoji."</span></button>";
			}
			mysqli_free_result($result);
		} else{ $cadena2 = "No hay datos colega...";		}
	} else{
		$cadena2 =  "ERROR: no se ha podido conectar a la base de datos.". mysqli_error($link);
	}
	mysqli_close($link);
	$titulo = "<H2>Listado de Provincias</H2>";
    return $titulo.$cadena;
}
add_shortcode('SC_PROVINCIAS','post_fun_provincias');
