<html>
<!-- jQuery -->
<script language="JavaScript" type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<!-- HighCharts -->
<script src="https://code.highcharts.com/highcharts.js"></script>
<script src="https://code.highcharts.com/modules/exporting.js"></script>
<script src="https://code.highcharts.com/maps/modules/map.js"></script>
<script src="https://code.highcharts.com/maps/modules/data.js"></script>
<script src="https://code.highcharts.com/maps/modules/exporting.js"></script>
<script src="https://code.highcharts.com/mapdata/custom/world.js"></script>
<!-- Data -->
<script src="/blog/js/dataAvgTemp.js"></script>
<!-- Style -->
<style>
 #yearTitle {
  color: #000;
  text-align: center;
 }
 .loading {
  margin-top: 10em;
  text-align: center;
  color: gray;
 }
</style>
<body>

Select Country
<select id="selectCountry">
 <option value="0">Afghanistan</option>
 <option value="1">Albania</option>
 <option value="2">Algeria</option>
 <option value="3">American Samoa</option>
 <option value="4">Andorra</option>
 <option value="5">Angola</option>
 <option value="6">Antigua And Barbuda</option>
 <option value="7">Argentina</option>
 <option value="8">Armenia</option>
 <option value="9">Aruba</option>
 <option value="10">Australia</option>
 <option value="11">Austria</option>
 <option value="12">Azerbaijan</option>
 <option value="13">Bahamas</option>
 <option value="14">Bahrain</option>
 <option value="15">Bangladesh</option>
 <option value="16">Barbados</option>
 <option value="17">Belarus</option>
 <option value="18">Belgium</option>
 <option value="19">Belize</option>
 <option value="20">Benin</option>
 <option value="21">Bhutan</option>
 <option value="22">Bolivia</option>
 <option value="23">Bosnia And Herzegovina</option>
 <option value="24">Botswana</option>
 <option value="25">Brazil</option>
 <option value="26">Bulgaria</option>
 <option value="27">Burkina Faso</option>
 <option value="28">Burundi</option>
 <option value="29">Cambodia</option>
 <option value="30">Cameroon</option>
 <option value="31">Canada</option>
 <option value="32">Cape Verde</option>
 <option value="33">Cayman Islands</option>
 <option value="34">Central African Republic</option>
 <option value="35">Chad</option>
 <option value="36">Chile</option>
 <option value="37">China</option>
 <option value="38">Colombia</option>
 <option value="39">Comoros</option>
 <option value="40">Dem. Rep. Congo</option>
 <option value="41">Rep. Congo</option>
 <option value="42">Costa Rica</option>
 <option value="43">Cote d'Ivoire</option>
 <option value="44">Croatia</option>
 <option value="45">Cuba</option>
 <option value="46">Curacao</option>
 <option value="47">Cyprus</option>
 <option value="48">Czech Republic</option>
 <option value="49">Denmark</option>
 <option value="50">Djibouti</option>
 <option value="51">Dominica</option>
 <option value="52">Dominican Republic</option>
 <option value="53">Ecuador</option>
 <option value="54">Egypt</option>
 <option value="55">El Salvador</option>
 <option value="56">Equatorial Guinea</option>
 <option value="57">Eritrea</option>
 <option value="58">Estonia</option>
 <option value="59">Ethiopia</option>
 <option value="60">Faroe Islands</option>
 <option value="61">Fiji</option>
 <option value="62">Finland</option>
 <option value="63">France</option>
 <option value="64">French Polynesia</option>
 <option value="65">Gabon</option>
 <option value="66">Gambia</option>
 <option value="67">Georgia</option>
 <option value="68">Germany</option>
 <option value="69">Ghana</option>
 <option value="70">Greece</option>
 <option value="71">Greenland</option>
 <option value="72">Grenada</option>
 <option value="73">Guam</option>
 <option value="74">Guatemala</option>
 <option value="75">Guinea</option>
 <option value="76">Guinea-Bissau</option>
 <option value="77">Haiti</option>
 <option value="78">Honduras</option>
 <option value="79">Hong Kong</option>
 <option value="80">Hungary</option>
 <option value="81">Iceland</option>
 <option value="82">India</option>
 <option value="83">Indonesia</option>
 <option value="84">Iran</option>
 <option value="85">Iraq</option>
 <option value="86">Ireland</option>
 <option value="87">Isle Of Man</option>
 <option value="88">Israel</option>
 <option value="89">Italy</option>
 <option value="90">Jamaica</option>
 <option value="91">Japan</option>
 <option value="92">Jordan</option>
 <option value="93">Kazakhstan</option>
 <option value="94">Kenya</option>
 <option value="95">Kiribati</option>
 <option value="96">North Korea</option>
 <option value="97">South Korea</option>
 <option value="98">Kuwait</option>
 <option value="99">Kyrgyzstan</option>
 <option value="100">Laos</option>
 <option value="101">Latvia</option>
 <option value="102">Lebanon</option>
 <option value="103">Lesotho</option>
 <option value="104">Liberia</option>
 <option value="105">Libya</option>
 <option value="106">Liechtenstein</option>
 <option value="107">Lithuania</option>
 <option value="108">Luxembourg</option>
 <option value="109">Macau</option>
 <option value="110">Macedonia</option>
 <option value="111">Madagascar</option>
 <option value="112">Malawi</option>
 <option value="113">Malaysia</option>
 <option value="114">Mali</option>
 <option value="115">Malta</option>
 <option value="116">Mauritania</option>
 <option value="117">Mauritius</option>
 <option value="118">Mayotte</option>
 <option value="119">Mexico</option>
 <option value="120">Moldova</option>
 <option value="121">Monaco</option>
 <option value="122">Mongolia</option>
 <option value="123">Montenegro</option>
 <option value="124">Morocco</option>
 <option value="125">Mozambique</option>
 <option value="126">Namibia</option>
 <option value="127">Nepal</option>
 <option value="128">Netherlands</option>
 <option value="129">New Caledonia</option>
 <option value="130">New Zealand</option>
 <option value="131">Nicaragua</option>
 <option value="132">Niger</option>
 <option value="133">Nigeria</option>
 <option value="134">Norway</option>
 <option value="135">Oman</option>
 <option value="136">Pakistan</option>
 <option value="137">Palau</option>
 <option value="138">Panama</option>
 <option value="139">Papua New Guinea</option>
 <option value="140">Paraguay</option>
 <option value="141">Peru</option>
 <option value="142">Philippines</option>
 <option value="143">Poland</option>
 <option value="144">Portugal</option>
 <option value="145">Puerto Rico</option>
 <option value="146">Qatar</option>
 <option value="147">Romania</option>
 <option value="148">Russia</option>
 <option value="149">Rwanda</option>
 <option value="150">Samoa</option>
 <option value="151">San Marino</option>
 <option value="152">Sao Tome And Principe</option>
 <option value="153">Saudi Arabia</option>
 <option value="154">Senegal</option>
 <option value="155">Serbia</option>
 <option value="156">Seychelles</option>
 <option value="157">Sierra Leone</option>
 <option value="158">Singapore</option>
 <option value="159">Slovakia</option>
 <option value="160">Slovenia</option>
 <option value="161">Solomon Islands</option>
 <option value="162">Somalia</option>
 <option value="163">South Africa</option>
 <option value="164">Spain</option>
 <option value="165">Sri Lanka</option>
 <option value="166">St. Kitts And Nevis</option>
 <option value="167">St. Lucia</option>
 <option value="168">St. Martin</option>
 <option value="169">St. Vincent And The Grenadines</option>
 <option value="170">Sudan</option>
 <option value="171">Suriname</option>
 <option value="172">Swaziland</option>
 <option value="173">Sweden</option>
 <option value="174">Switzerland</option>
 <option value="175">Syria</option>
 <option value="176">Tajikistan</option>
 <option value="177">Tanzania</option>
 <option value="178">Thailand</option>
 <option value="179">Timor-Leste</option>
 <option value="180">Togo</option>
 <option value="181">Tonga</option>
 <option value="182">Trinidad And Tobago</option>
 <option value="183">Tunisia</option>
 <option value="184">Turkey</option>
 <option value="185">Turkmenistan</option>
 <option value="186">Turks And Caicas Islands</option>
 <option value="187">Uganda</option>
 <option value="188">Ukraine</option>
 <option value="189">United Arab Emirates</option>
 <option value="190">United Kingdom</option>
 <option value="191">United States</option>
 <option value="192">Uruguay</option>
 <option value="193">Uzbekistan</option>
 <option value="194">Venezuela</option>
 <option value="195">Vietnam</option>
 <option value="196">Virgin Islands</option>
 <option value="197">Western Sahara</option>
 <option value="198">Yemen</option>
 <option value="199">Zambia</option>
 <option value="200">Zimbabwe</option>
</select>

<div id="container1" style="height: 500px"></div>
<br>
<br>
Select two countries to compare<br>
First Country
<select id="selectCountry1">
 <option value="0">Afghanistan</option>
 <option value="1">Albania</option>
 <option value="2">Algeria</option>
 <option value="3">American Samoa</option>
 <option value="4">Andorra</option>
 <option value="5">Angola</option>
 <option value="6">Antigua And Barbuda</option>
 <option value="7">Argentina</option>
 <option value="8">Armenia</option>
 <option value="9">Aruba</option>
 <option value="10">Australia</option>
 <option value="11">Austria</option>
 <option value="12">Azerbaijan</option>
 <option value="13">Bahamas</option>
 <option value="14">Bahrain</option>
 <option value="15">Bangladesh</option>
 <option value="16">Barbados</option>
 <option value="17">Belarus</option>
 <option value="18">Belgium</option>
 <option value="19">Belize</option>
 <option value="20">Benin</option>
 <option value="21">Bhutan</option>
 <option value="22">Bolivia</option>
 <option value="23">Bosnia And Herzegovina</option>
 <option value="24">Botswana</option>
 <option value="25">Brazil</option>
 <option value="26">Bulgaria</option>
 <option value="27">Burkina Faso</option>
 <option value="28">Burundi</option>
 <option value="29">Cambodia</option>
 <option value="30">Cameroon</option>
 <option value="31">Canada</option>
 <option value="32">Cape Verde</option>
 <option value="33">Cayman Islands</option>
 <option value="34">Central African Republic</option>
 <option value="35">Chad</option>
 <option value="36">Chile</option>
 <option value="37">China</option>
 <option value="38">Colombia</option>
 <option value="39">Comoros</option>
 <option value="40">Dem. Rep. Congo</option>
 <option value="41">Rep. Congo</option>
 <option value="42">Costa Rica</option>
 <option value="43">Cote d'Ivoire</option>
 <option value="44">Croatia</option>
 <option value="45">Cuba</option>
 <option value="46">Curacao</option>
 <option value="47">Cyprus</option>
 <option value="48">Czech Republic</option>
 <option value="49">Denmark</option>
 <option value="50">Djibouti</option>
 <option value="51">Dominica</option>
 <option value="52">Dominican Republic</option>
 <option value="53">Ecuador</option>
 <option value="54">Egypt</option>
 <option value="55">El Salvador</option>
 <option value="56">Equatorial Guinea</option>
 <option value="57">Eritrea</option>
 <option value="58">Estonia</option>
 <option value="59">Ethiopia</option>
 <option value="60">Faroe Islands</option>
 <option value="61">Fiji</option>
 <option value="62">Finland</option>
 <option value="63">France</option>
 <option value="64">French Polynesia</option>
 <option value="65">Gabon</option>
 <option value="66">Gambia</option>
 <option value="67">Georgia</option>
 <option value="68">Germany</option>
 <option value="69">Ghana</option>
 <option value="70">Greece</option>
 <option value="71">Greenland</option>
 <option value="72">Grenada</option>
 <option value="73">Guam</option>
 <option value="74">Guatemala</option>
 <option value="75">Guinea</option>
 <option value="76">Guinea-Bissau</option>
 <option value="77">Haiti</option>
 <option value="78">Honduras</option>
 <option value="79">Hong Kong</option>
 <option value="80">Hungary</option>
 <option value="81">Iceland</option>
 <option value="82">India</option>
 <option value="83">Indonesia</option>
 <option value="84">Iran</option>
 <option value="85">Iraq</option>
 <option value="86">Ireland</option>
 <option value="87">Isle Of Man</option>
 <option value="88">Israel</option>
 <option value="89">Italy</option>
 <option value="90">Jamaica</option>
 <option value="91">Japan</option>
 <option value="92">Jordan</option>
 <option value="93">Kazakhstan</option>
 <option value="94">Kenya</option>
 <option value="95">Kiribati</option>
 <option value="96">North Korea</option>
 <option value="97">South Korea</option>
 <option value="98">Kuwait</option>
 <option value="99">Kyrgyzstan</option>
 <option value="100">Laos</option>
 <option value="101">Latvia</option>
 <option value="102">Lebanon</option>
 <option value="103">Lesotho</option>
 <option value="104">Liberia</option>
 <option value="105">Libya</option>
 <option value="106">Liechtenstein</option>
 <option value="107">Lithuania</option>
 <option value="108">Luxembourg</option>
 <option value="109">Macau</option>
 <option value="110">Macedonia</option>
 <option value="111">Madagascar</option>
 <option value="112">Malawi</option>
 <option value="113">Malaysia</option>
 <option value="114">Mali</option>
 <option value="115">Malta</option>
 <option value="116">Mauritania</option>
 <option value="117">Mauritius</option>
 <option value="118">Mayotte</option>
 <option value="119">Mexico</option>
 <option value="120">Moldova</option>
 <option value="121">Monaco</option>
 <option value="122">Mongolia</option>
 <option value="123">Montenegro</option>
 <option value="124">Morocco</option>
 <option value="125">Mozambique</option>
 <option value="126">Namibia</option>
 <option value="127">Nepal</option>
 <option value="128">Netherlands</option>
 <option value="129">New Caledonia</option>
 <option value="130">New Zealand</option>
 <option value="131">Nicaragua</option>
 <option value="132">Niger</option>
 <option value="133">Nigeria</option>
 <option value="134">Norway</option>
 <option value="135">Oman</option>
 <option value="136">Pakistan</option>
 <option value="137">Palau</option>
 <option value="138">Panama</option>
 <option value="139">Papua New Guinea</option>
 <option value="140">Paraguay</option>
 <option value="141">Peru</option>
 <option value="142">Philippines</option>
 <option value="143">Poland</option>
 <option value="144">Portugal</option>
 <option value="145">Puerto Rico</option>
 <option value="146">Qatar</option>
 <option value="147">Romania</option>
 <option value="148">Russia</option>
 <option value="149">Rwanda</option>
 <option value="150">Samoa</option>
 <option value="151">San Marino</option>
 <option value="152">Sao Tome And Principe</option>
 <option value="153">Saudi Arabia</option>
 <option value="154">Senegal</option>
 <option value="155">Serbia</option>
 <option value="156">Seychelles</option>
 <option value="157">Sierra Leone</option>
 <option value="158">Singapore</option>
 <option value="159">Slovakia</option>
 <option value="160">Slovenia</option>
 <option value="161">Solomon Islands</option>
 <option value="162">Somalia</option>
 <option value="163">South Africa</option>
 <option value="164">Spain</option>
 <option value="165">Sri Lanka</option>
 <option value="166">St. Kitts And Nevis</option>
 <option value="167">St. Lucia</option>
 <option value="168">St. Martin</option>
 <option value="169">St. Vincent And The Grenadines</option>
 <option value="170">Sudan</option>
 <option value="171">Suriname</option>
 <option value="172">Swaziland</option>
 <option value="173">Sweden</option>
 <option value="174">Switzerland</option>
 <option value="175">Syria</option>
 <option value="176">Tajikistan</option>
 <option value="177">Tanzania</option>
 <option value="178">Thailand</option>
 <option value="179">Timor-Leste</option>
 <option value="180">Togo</option>
 <option value="181">Tonga</option>
 <option value="182">Trinidad And Tobago</option>
 <option value="183">Tunisia</option>
 <option value="184">Turkey</option>
 <option value="185">Turkmenistan</option>
 <option value="186">Turks And Caicas Islands</option>
 <option value="187">Uganda</option>
 <option value="188">Ukraine</option>
 <option value="189">United Arab Emirates</option>
 <option value="190">United Kingdom</option>
 <option value="191">United States</option>
 <option value="192">Uruguay</option>
 <option value="193">Uzbekistan</option>
 <option value="194">Venezuela</option>
 <option value="195">Vietnam</option>
 <option value="196">Virgin Islands</option>
 <option value="197">Western Sahara</option>
 <option value="198">Yemen</option>
 <option value="199">Zambia</option>
 <option value="200">Zimbabwe</option>
</select>
<br>Second Country
<select id="selectCountry2">
 <option value="0">Afghanistan</option>
 <option value="1">Albania</option>
 <option value="2">Algeria</option>
 <option value="3">American Samoa</option>
 <option value="4">Andorra</option>
 <option value="5">Angola</option>
 <option value="6">Antigua And Barbuda</option>
 <option value="7">Argentina</option>
 <option value="8">Armenia</option>
 <option value="9">Aruba</option>
 <option value="10">Australia</option>
 <option value="11">Austria</option>
 <option value="12">Azerbaijan</option>
 <option value="13">Bahamas</option>
 <option value="14">Bahrain</option>
 <option value="15">Bangladesh</option>
 <option value="16">Barbados</option>
 <option value="17">Belarus</option>
 <option value="18">Belgium</option>
 <option value="19">Belize</option>
 <option value="20">Benin</option>
 <option value="21">Bhutan</option>
 <option value="22">Bolivia</option>
 <option value="23">Bosnia And Herzegovina</option>
 <option value="24">Botswana</option>
 <option value="25">Brazil</option>
 <option value="26">Bulgaria</option>
 <option value="27">Burkina Faso</option>
 <option value="28">Burundi</option>
 <option value="29">Cambodia</option>
 <option value="30">Cameroon</option>
 <option value="31">Canada</option>
 <option value="32">Cape Verde</option>
 <option value="33">Cayman Islands</option>
 <option value="34">Central African Republic</option>
 <option value="35">Chad</option>
 <option value="36">Chile</option>
 <option value="37">China</option>
 <option value="38">Colombia</option>
 <option value="39">Comoros</option>
 <option value="40">Dem. Rep. Congo</option>
 <option value="41">Rep. Congo</option>
 <option value="42">Costa Rica</option>
 <option value="43">Cote d'Ivoire</option>
 <option value="44">Croatia</option>
 <option value="45">Cuba</option>
 <option value="46">Curacao</option>
 <option value="47">Cyprus</option>
 <option value="48">Czech Republic</option>
 <option value="49">Denmark</option>
 <option value="50">Djibouti</option>
 <option value="51">Dominica</option>
 <option value="52">Dominican Republic</option>
 <option value="53">Ecuador</option>
 <option value="54">Egypt</option>
 <option value="55">El Salvador</option>
 <option value="56">Equatorial Guinea</option>
 <option value="57">Eritrea</option>
 <option value="58">Estonia</option>
 <option value="59">Ethiopia</option>
 <option value="60">Faroe Islands</option>
 <option value="61">Fiji</option>
 <option value="62">Finland</option>
 <option value="63">France</option>
 <option value="64">French Polynesia</option>
 <option value="65">Gabon</option>
 <option value="66">Gambia</option>
 <option value="67">Georgia</option>
 <option value="68">Germany</option>
 <option value="69">Ghana</option>
 <option value="70">Greece</option>
 <option value="71">Greenland</option>
 <option value="72">Grenada</option>
 <option value="73">Guam</option>
 <option value="74">Guatemala</option>
 <option value="75">Guinea</option>
 <option value="76">Guinea-Bissau</option>
 <option value="77">Haiti</option>
 <option value="78">Honduras</option>
 <option value="79">Hong Kong</option>
 <option value="80">Hungary</option>
 <option value="81">Iceland</option>
 <option value="82">India</option>
 <option value="83">Indonesia</option>
 <option value="84">Iran</option>
 <option value="85">Iraq</option>
 <option value="86">Ireland</option>
 <option value="87">Isle Of Man</option>
 <option value="88">Israel</option>
 <option value="89">Italy</option>
 <option value="90">Jamaica</option>
 <option value="91">Japan</option>
 <option value="92">Jordan</option>
 <option value="93">Kazakhstan</option>
 <option value="94">Kenya</option>
 <option value="95">Kiribati</option>
 <option value="96">North Korea</option>
 <option value="97">South Korea</option>
 <option value="98">Kuwait</option>
 <option value="99">Kyrgyzstan</option>
 <option value="100">Laos</option>
 <option value="101">Latvia</option>
 <option value="102">Lebanon</option>
 <option value="103">Lesotho</option>
 <option value="104">Liberia</option>
 <option value="105">Libya</option>
 <option value="106">Liechtenstein</option>
 <option value="107">Lithuania</option>
 <option value="108">Luxembourg</option>
 <option value="109">Macau</option>
 <option value="110">Macedonia</option>
 <option value="111">Madagascar</option>
 <option value="112">Malawi</option>
 <option value="113">Malaysia</option>
 <option value="114">Mali</option>
 <option value="115">Malta</option>
 <option value="116">Mauritania</option>
 <option value="117">Mauritius</option>
 <option value="118">Mayotte</option>
 <option value="119">Mexico</option>
 <option value="120">Moldova</option>
 <option value="121">Monaco</option>
 <option value="122">Mongolia</option>
 <option value="123">Montenegro</option>
 <option value="124">Morocco</option>
 <option value="125">Mozambique</option>
 <option value="126">Namibia</option>
 <option value="127">Nepal</option>
 <option value="128">Netherlands</option>
 <option value="129">New Caledonia</option>
 <option value="130">New Zealand</option>
 <option value="131">Nicaragua</option>
 <option value="132">Niger</option>
 <option value="133">Nigeria</option>
 <option value="134">Norway</option>
 <option value="135">Oman</option>
 <option value="136">Pakistan</option>
 <option value="137">Palau</option>
 <option value="138">Panama</option>
 <option value="139">Papua New Guinea</option>
 <option value="140">Paraguay</option>
 <option value="141">Peru</option>
 <option value="142">Philippines</option>
 <option value="143">Poland</option>
 <option value="144">Portugal</option>
 <option value="145">Puerto Rico</option>
 <option value="146">Qatar</option>
 <option value="147">Romania</option>
 <option value="148">Russia</option>
 <option value="149">Rwanda</option>
 <option value="150">Samoa</option>
 <option value="151">San Marino</option>
 <option value="152">Sao Tome And Principe</option>
 <option value="153">Saudi Arabia</option>
 <option value="154">Senegal</option>
 <option value="155">Serbia</option>
 <option value="156">Seychelles</option>
 <option value="157">Sierra Leone</option>
 <option value="158">Singapore</option>
 <option value="159">Slovakia</option>
 <option value="160">Slovenia</option>
 <option value="161">Solomon Islands</option>
 <option value="162">Somalia</option>
 <option value="163">South Africa</option>
 <option value="164">Spain</option>
 <option value="165">Sri Lanka</option>
 <option value="166">St. Kitts And Nevis</option>
 <option value="167">St. Lucia</option>
 <option value="168">St. Martin</option>
 <option value="169">St. Vincent And The Grenadines</option>
 <option value="170">Sudan</option>
 <option value="171">Suriname</option>
 <option value="172">Swaziland</option>
 <option value="173">Sweden</option>
 <option value="174">Switzerland</option>
 <option value="175">Syria</option>
 <option value="176">Tajikistan</option>
 <option value="177">Tanzania</option>
 <option value="178">Thailand</option>
 <option value="179">Timor-Leste</option>
 <option value="180">Togo</option>
 <option value="181">Tonga</option>
 <option value="182">Trinidad And Tobago</option>
 <option value="183">Tunisia</option>
 <option value="184">Turkey</option>
 <option value="185">Turkmenistan</option>
 <option value="186">Turks And Caicas Islands</option>
 <option value="187">Uganda</option>
 <option value="188">Ukraine</option>
 <option value="189">United Arab Emirates</option>
 <option value="190">United Kingdom</option>
 <option value="191">United States</option>
 <option value="192">Uruguay</option>
 <option value="193">Uzbekistan</option>
 <option value="194">Venezuela</option>
 <option value="195">Vietnam</option>
 <option value="196">Virgin Islands</option>
 <option value="197">Western Sahara</option>
 <option value="198">Yemen</option>
 <option value="199">Zambia</option>
 <option value="200">Zimbabwe</option>
</select>

<div id="container2" style="height: 500px"></div>

<br>
<br>
<h1 id="yearTitle">1990</h1>
<div id="container3" style="height: 600px; margin: 0 auto;"></div>

</body>

<script>
$(function () {

 // CHART 1 //
 var options1 = {
  chart: {
   renderTo: 'container1',
   defaultSeriesType: 'spline'
  },
  title: {
            text: 'Average Temperature',
            x: -20 //center
        },
        subtitle: {
            text: '1900 - 2013',
            x: -20
        },
        xAxis: {
            categories: dataYear
        },
        yAxis: {
            title: {
                text: 'Temperature (Â°C)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: 'Â°C'
        },
  series: [{
   name: 'Average World Temparature',
   data: avgWorld
  },
  {
   name: dataCountry[0],
   data: dataLocal[0]
  }]
 };
 
 var chart1 = new Highcharts.Chart(options1);

 $("#selectCountry").on('change', function(){
  var dropdownVal = $("#selectCountry").val();
  options1.series = [{
   name: 'Average World Temparature',
   data: avgWorld
  },
  {
   name: dataCountry[dropdownVal],
   data: dataLocal[dropdownVal]
  }];
  var chart1 = new Highcharts.Chart(options1);    
 });
 
 // CHART 2 //
 var options2 = {
  chart: {
   renderTo: 'container2',
   defaultSeriesType: 'spline'
  },
  title: {
            text: 'Compare Average Temperature',
            x: -20 //center
        },
        subtitle: {
            text: 'For 2 countries',
            x: -20
        },
        xAxis: {
            categories: dataYear
        },
        yAxis: {
            title: {
                text: 'Temperature (Â°C)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: 'Â°C'
        },
  series: [{
   name: 'Average World Temparature',
   data: avgWorld
  },
  {
   name: dataCountry[0],
   data: dataLocal[0]
  },
  {
   name: dataCountry[1],
   data: dataLocal[1]
  }]
 };
 
 var chart2 = new Highcharts.Chart(options2);

 $("#selectCountry1").on('change', function(){
  var dropdownVal1 = $("#selectCountry1").val();
  var dropdownVal2 = $("#selectCountry2").val();
  options2.series = [{
   name: 'Average World Temparature',
   data: avgWorld
  },
  {
   name: dataCountry[dropdownVal1],
   data: dataLocal[dropdownVal1]
  },
  {
   name: dataCountry[dropdownVal2],
   data: dataLocal[dropdownVal2]
  }];
  var chart2 = new Highcharts.Chart(options2);    
 });
  
 $("#selectCountry2").on('change', function(){
  var dropdownVal1 = $("#selectCountry1").val();
  var dropdownVal2 = $("#selectCountry2").val();
  options2.series = [{
   name: 'Average World Temparature',
   data: avgWorld
  },
  {
   name: dataCountry[dropdownVal1],
   data: dataLocal[dropdownVal1]
  },
  {
   name: dataCountry[dropdownVal2],
   data: dataLocal[dropdownVal2]
  }];
  var chart2 = new Highcharts.Chart(options2);    
 });
 
 // World Map //
 dataPos = 0;

 $('#container3').highcharts('Map', {

  title : {
   text : 'Average temperature per country per year'
  },

  /*mapNavigation: {
   enabled: true,
   enableDoubleClickZoomTo: true
  },*/

  colorAxis: {
   min: -25,
   max: 35,
   type: 'linear',//'logarithmic'
   minColor: '#0000FF',
   maxColor: '#FF0000'
  },

  series : [{
   data : dataMap[dataPos],
   mapData: Highcharts.maps['custom/world'],
   joinBy: ['iso-a2', 'code'],
   name:  'Average Temperature',
   states: {
    hover: {
     color: '#BADA55'
    }
   },
   tooltip: {
    valueSuffix: 'deg'
   }
  }]
 });
 
 setInterval(function () {
  chart = $('#container3').highcharts();
  chart.series[0].setData(dataMap[dataPos]);
  document.getElementById("yearTitle").innerHTML = (dataPos+1900).toString();
  dataPos++;
  if( dataPos == 113 )
   dataPos = 0;
 },1000 );
});
</script>

</html>
