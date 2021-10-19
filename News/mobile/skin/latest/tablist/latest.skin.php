<?php
if (!defined('_GNUBOARD_')) exit; // 개별 페이지 접근 불가
// add_stylesheet('css 구문', 출력순서); 숫자가 작을 수록 먼저 출력됨
add_stylesheet('<link rel="stylesheet" href="'.$latest_skin_url.'/style.css">', 0);
?>

<!-- <?php echo $bo_subject; ?> 최신글 시작 { -->
<div id="tablist">
  <div class="list-tab">
  		<ul>
    		<?php for ($i=0; $i<count($list); $i++) {  ?>
           	 <?php
            	//echo $list[$i]['icon_reply']." ";
				echo "<li>";
           	 	echo "<a href=\"".$list[$i]['href']."\">";
            	if ($list[$i]['is_notice'])
                	echo "<strong>".$list[$i]['subject']."</strong>";
            	else
                	echo $list[$i]['subject'];

            	if ($list[$i]['comment_cnt'])
                	echo $list[$i]['comment_cnt'];

            	echo "</a>";

            	/*/ if ($list[$i]['link']['count']) { echo "[{$list[$i]['link']['count']}]"; }
            	// if ($list[$i]['file']['count']) { echo "<{$list[$i]['file']['count']}>"; }

            	if (isset($list[$i]['icon_new'])) echo " " . $list[$i]['icon_new'];
            	if (isset($list[$i]['icon_hot'])) echo " " . $list[$i]['icon_hot'];
            	if (isset($list[$i]['icon_file'])) echo " " . $list[$i]['icon_file'];
            	if (isset($list[$i]['icon_link'])) echo " " . $list[$i]['icon_link'];
            	if (isset($list[$i]['icon_secret'])) echo " " . $list[$i]['icon_secret'];*/
			

				echo "<span>".date("m-d", strtotime($list[$i]['wr_datetime']))."</span>";
				echo "</li>";
             	?>
             	<?php if (count($list) == 0) { //게시물이 없을 때 
       				echo "<li><a href='#'>게시물이 없습니다.</a><span>0000-00-00</span></li>";
        			} 
				}
			?>
		</ul>
	</div>
</div>
<!-- } <?php echo $bo_subject; ?> 최신글 끝 -->